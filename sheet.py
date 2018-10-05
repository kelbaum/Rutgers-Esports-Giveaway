from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import reference
import main

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'


# retrieves sheet
def get_sheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    result = service.spreadsheets().values().get(spreadsheetId=reference.SPREADSHEET_ID,
                                                range=reference.RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return []
    else:
        # print all names and phone #s
        # print('Name, Phone #:')
        '''
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            if len(row) != 3:
                # print('%s' % (row[1]))
                continue
            # print('%s, %s' % (row[1], row[2]))
        '''
        print("Entrants are loaded.")
        return values


# A person (entry) is selected from 'values'
def select_person(query, officers, new_officers, officers_banned, new_officers_banned):
    # print(len(query))
    if len(query) == 0:
        print("The query is empty!")
        return []
    # add loop here for rerolls
    if officers_banned is True and new_officers_banned is True:
        while True:
            index = main.roll(len(query))
            if query[index][1] not in officers or query[index][1] not in new_officers:
                break
    elif officers_banned is True:
        while True:
            index = main.roll(len(query))
            if query[index][1] not in officers:
                break
    elif new_officers_banned is True:
        while True:
            index = main.roll(len(query))
            if query[index][1] not in new_officers:
                break
    else:
        index = main.roll(len(query))

    # print(query[index])
    print("Winner: " + query[index][1])
    return query[index]
