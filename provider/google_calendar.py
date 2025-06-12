from typing import Any
import json

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from google.oauth2 import service_account


class GoogleCalendarProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            credentials_json = credentials.get('credentials_json')
            
            if not credentials_json:
                raise ValueError("Missing required credentials: credentials_json is required")

            try:
                service_account_info = json.loads(credentials_json)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format for credentials_json")

            required_fields = ['client_email', 'private_key', 'type']
            missing_fields = [field for field in required_fields if field not in service_account_info]
            if missing_fields:
                raise ValueError(f"Missing required fields in credentials_json: {', '.join(missing_fields)}")

            if service_account_info.get('type') != 'service_account':
                raise ValueError("Invalid credentials type, must be 'service_account'")
            
            service_account.Credentials.from_service_account_info(
                service_account_info, 
                scopes=['https://www.googleapis.com/auth/calendar']
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
