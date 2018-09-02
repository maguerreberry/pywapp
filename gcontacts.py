from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

os.chdir('C:\\Users\\matt_\\eclipse-workspace\\wapp')

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/contacts.readonly'

"""Shows basic usage of the People API.
Prints the name of the first 10 connections.
"""
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('people', 'v1', http=creds.authorize(Http()))
# Call the People API
print('List 100 connection names')
results = service.people().connections().list(
    resourceName='people/me',
    pageSize=2000,
    personFields='names,memberships',
    sortOrder='FIRST_NAME_ASCENDING').execute()
connections = results.get('connections', [])

for person in connections:
    names = person.get('names', [])
    memberships = person.get('memberships', [])
    if names:
        name = names[0].get('displayName')
        memberships
        print(name)

