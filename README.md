# Gsheet processing tool
Goal of this utility is to 
1. read a gsheet(source)
2. copy selected columns to another gsheet(target) 
3. if there are more columns in another gsheet those should remain untouched.

The first sheet is the master sheet which contains all information. Only some information is relevant for human users. That is extracted into a second sheet. Human users can then add some more notes(columns) into the second sheet. Those notes should not be overwritten if we rerun this tool. If there are new rows in the first sheet when we rerun this tool it should be copied to the second sheet.

## Implementation details
1. create both source sheet and target sheet
2. get sheet id and create a .env file with it
3. 
