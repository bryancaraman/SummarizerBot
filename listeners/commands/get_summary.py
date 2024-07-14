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
        "prompt": "I am giving you a list of messages that include three types of data: the message text, a link to the message, and username.\nYou need to summarize the text of these messages so that someone can quickly understand what has been talked about. Separate different conversations into different points and return a message as a bulleted list of all the different topics/conversations.\nIf there are only one or two conversations/topics, do not return a bulleted list, just summarize it and format it in a paragraph or two. If there are very few messages to summarize or there is nothing interesting or importance, return 'Nothing important to summarize.'\nWhen returning the summary, include the link of the first message in a specific conversation/topic formatted like this after the summary:\nLink to conversation: 'hyperlink'. Do not do anything with the users provided.\nConversation history:" f"{conversation_data}",
        "provider": "openai_chat",
        "providerOptions": {
            "model": "gpt-3.5-turbo"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['data']['value']
