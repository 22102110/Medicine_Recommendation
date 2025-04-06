from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']

def generate_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES
    )

    # Set the correct redirect URI
    creds = flow.run_local_server(port=5001)

    # Save the token
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    print("✅ token.json has been generated successfully!")


if __name__ == "__main__":
    generate_token()

