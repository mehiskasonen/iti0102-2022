"""API."""

from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from urllib.parse import parse_qs, urlparse

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M'
SAMPLE_RANGE_NAME = 'A1:A10'


def get_links_from_spreadsheet(id: str, token_file_name: str) -> list:
    """Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    creds = None
    res = []
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file_name, 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            res += row
    return res


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.
    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    url = link
    query = parse_qs(urlparse(url).query, keep_blank_values=True)
    playlist_id = query["list"][0]

    youtube = build('youtube', 'v3', developerKey=developer_key)

    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
    )

    playlist_items = []
    result = []
    while request is not None:
        response = request.execute()
        playlist_items += response["items"]
        request = youtube.playlistItems().list_next(request, response)

    for t in playlist_items:
        result += [f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s']
    return result


if __name__ == '__main__':
    print(get_links_from_spreadsheet(
        'https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M/edit#gid=0',
        '1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M'))

