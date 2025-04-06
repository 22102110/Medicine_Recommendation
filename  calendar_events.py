from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def list_events():
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("calendar", "v3", credentials=creds)

    # Get upcoming 10 events
    events_result = service.events().list(
        calendarId="primary", maxResults=10, singleEvents=True,
        orderBy="startTime").execute()

    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
        return

    print("Upcoming events:")
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(f"{start} - {event['summary']}")

if __name__ == "__main__":
    list_events()
