import requests
import json
from config import jwt

def get_summary(conversation):
    # Endpoint for request
    url = 'https://caas.api.godaddy.com/v1/prompts'

    headers = {
        'Authorization': f'sso-jwt {jwt}',
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    conversation_data = []

    for message in conversation:
        conversation_data.append(message.message_data)

    # Body of request
    data = {
        "prompt": "I am giving you a list of messages that include three types of data: the message text, ts, and username.\nYou need to summarize these messages so that someone can quickly understand what has been talked about. Separate different conversations into different points and return a message as a bulleted list of all the different topics/conversations. When returning the summary, include the ts of the first message in a specific conversation. Do not do anything with the user_name provided.\nConversation history:" f"{conversation_data}",
        "provider": "openai_chat",
        "providerOptions": {
            "model": "gpt-3.5-turbo"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['data']['value']
