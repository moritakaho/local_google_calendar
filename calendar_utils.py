from google.oauth2 import service_account
import json

class GoogleCalendarUtils:
    
    @staticmethod
    def get_credentials(credentials_json: str) -> service_account.Credentials:
        """
        Google Calendar API 用のサービスアカウント認証情報を取得

        Parameters
        ----------
        credentials_json : str
            認証情報

        Returns
        -------
        service_account.Credentials
            Google Calendar API 用のサービスアカウント認証情報
        """
        try:
            credentials_info = json.loads(credentials_json)

            credentials = service_account.Credentials.from_service_account_info(
                credentials_info,
                scopes=['https://www.googleapis.com/auth/calendar']
            )
            
            return credentials
        except Exception as e:
            raise Exception(f"Failed to create credentials: {str(e)}")
