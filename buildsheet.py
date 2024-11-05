import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SAMPLE_SPREADSHEET_SHEET_ID = '1_AuqQbTAwZf0EfM5Zu4e_VCjze4Rqn3JwEryGOXFB6M'
SAMPLE_RANGE_NAME = 'Sheet1!A1'

class BuildSheet:
    def __init__(self):
        self.creds = self.build_creds()


    def build_creds(self):
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and self.creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return creds

    def insert_data(self, creds, insert_list, configs):
        patient_list = []
        patient_headings = ["Name", "Compliance", "Percentage", "Serial Number"]
        patient_list.append(patient_headings)
        for item in insert_list:
            patient_list.append([item['Name'], item['Compliance'], item['Percentage'], item['SerialNumber']])

        try:
            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()
            result = sheet.values().update(spreadsheetId=configs['output_spreadsheet'], range=SAMPLE_RANGE_NAME, valueInputOption='USER_ENTERED', body={'values': patient_list}).execute()
        except HttpError as err:
            print(err)







