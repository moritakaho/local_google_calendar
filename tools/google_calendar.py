from typing import Any, Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from calendar_utils import GoogleCalendarUtils
from googleapiclient.discovery import build

class GoogleCalendarTool(Tool):
    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        Google Calendarへの新規イベント登録
    
        Parameters
        ----------
        tool_parameters : dict[str, Any]
            カレンダーイベント作成に必要なパラメータ

        Yields
        ------
        Generator[ToolInvokeMessage, None, None]
            処理結果を示すメッセージのジェネレーター
        """
        calendar_id = tool_parameters.get("calendar_id", "primary")  
        summary = tool_parameters.get("summary", "")
        start_time = tool_parameters.get("start_time", "")
        end_time = tool_parameters.get("end_time", "")
        description = tool_parameters.get("description", "")
        time_zone = tool_parameters.get("time_zone", "Asia/Tokyo")
        location = tool_parameters.get("location", "")
        
        if not summary:
            yield self.create_text_message("Error: Calendar summary (title) is required")
            return
            
        try:
            credentials_json = self.runtime.credentials["credentials_json"]
            creds = GoogleCalendarUtils.get_credentials(credentials_json)

            service = build('calendar', 'v3', credentials=creds)

            event = {
                'summary': summary,
                'start': {
                    'dateTime': start_time,
                    'timeZone': time_zone,
                },
                'end': {
                    'dateTime': end_time,
                    'timeZone': time_zone,
                },
            }
            if description:
                event["description"] = description   
            if location:
                event["location"] = location

            created_event = service.events().insert(
                calendarId=calendar_id,
                body=event
            ).execute()
            
            result = {
                "id": created_event.get("id"),
                "summary": created_event.get("summary"),
                "start": created_event.get("start"),
                "end": created_event.get("end"),
                "htmlLink": created_event.get("htmlLink"),
                "success": True
            }
                
            yield self.create_text_message(f"Calendar '{summary}' created successfully")
            yield self.create_json_message(result)
        except Exception as e:
            error_message = f"Error creating calendar: {str(e)}"
            print(f"Error details: {error_message}")
            yield self.create_text_message(error_message)
