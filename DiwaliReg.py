import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

# Set up credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('utsav.json', scopes = scope)
gc = gspread.authorize(credentials)

# Pull data from original google sheet
sheet_id = "1fWuFKySxg08LYTT7-xBKAY6YuU12JJW3S7CNqrWIKqE"
sheet_name = "FormResponses"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
formResponses = pd.read_csv(url)
#formResponses = pd.read_csv(url, on_bad_lines='skip')

# Modify original data
extractedResponse = formResponses.iloc[:, [1, 2, 3, 4, 5, 7, 8, 9, 10]]

# Push to another google sheet
newSheetId = '1BRNKkIXHAJTkhk_XA4q_biKQSEfWT_w4c2fpcbPYG3M'
worksheet = 'EventInfo'

# Save the original Notes and add them back into the dataframe
newUrl = f"https://docs.google.com/spreadsheets/d/{newSheetId}/gviz/tq?tqx=out:csv&sheet={worksheet}"
reducedResponse = pd.read_csv(newUrl)
extractedResponse['Notes'] = reducedResponse['Notes']
# Replace nan with empty string
extractedResponse = extractedResponse.fillna('')

# Push to new google sheet
d2g.upload(extractedResponse, newSheetId, worksheet, credentials=credentials, row_names=False)

pass