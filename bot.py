import requests
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_TOKEN = '123'
CHANNEL_ID = 'C078NKRRY5P'


METAR_TAF_API_KEY = 'YOUR_API_KEY'
params = {
    'api_key': METAR_TAF_API_KEY,
    'v': '2.3',
    'locale': 'en-US',
    'id': 'LEMD'
}
url = 'https://api.metar-taf.com/metar'


def send_message_to_slack(channel_id, text):
    client = WebClient(token=SLACK_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text=text
        )
        return response
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")
        return None

try:
    response = requests.get(url, params=params, verify=False)
    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4)
        message = f"Response from Metar-TAF API:\n```{formatted_data}```"
        send_message_to_slack(CHANNEL_ID, message)
        print("Message sent successfully to Slack!")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    some text 
    