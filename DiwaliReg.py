import pandas as pd
import gspread
from dotenv import load_dotenv
import os
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()
credentials_json = os.getenv("CREDENTIALS_JSON", 'account_credentials.json')

sheet_id = os.getenv("SHEET_ID")
if sheet_id is None:
    print('SHEET_ID env variable is mandatory')

target_sheet_id = os.getenv("TARGET_SHEET_ID")
if target_sheet_id is None:
    print('TARGET_SHEET_ID env variable is mandatory')

worksheet = os.getenv("WORKSHEET_NAME")
if worksheet is None:
    print('WORKSHEET_NAME env variable is mandatory')



# Set up credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_json, scopes = scope)
gc = gspread.authorize(credentials)

# Pull data from original google sheet
sheet_name = "FormResponses"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
formResponses = pd.read_csv(url)
#formResponses = pd.read_csv(url, on_bad_lines='skip')

# Modify original data
extractedResponse = formResponses.iloc[:, [1, 2, 3, 4, 5, 7, 8, 9, 10]]

# Push to another google sheet


# Save the original Notes and add them back into the dataframe
newUrl = f"https://docs.google.com/spreadsheets/d/{target_sheet_id}/gviz/tq?tqx=out:csv&sheet={worksheet}"
reducedResponse = pd.read_csv(newUrl)
extractedResponse['Notes'] = reducedResponse['Notes']
# Replace nan with empty string
extractedResponse = extractedResponse.fillna('')

# Push to new google sheet
d2g.upload(extractedResponse, target_sheet_id, worksheet, credentials=credentials, row_names=False)

pass