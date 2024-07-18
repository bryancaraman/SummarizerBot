import requests
from config import JWT

def get_summary(conversation):
    # Endpoint for request
    url = 'https://caas.api.godaddy.com/v1/prompts'

    headers = {
        'Authorization': f'sso-jwt {JWT}',
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    conversation_data = []

    for message in conversation:
        conversation_data.append(message.message_data)

    # Body of request
    data = {
        "prompt": "I am giving you a list of messages that include two types of data: the message text, and a link to the message.\nYou need to summarize the text of these messages so that someone can quickly understand what has been talked about. Strictly use the information provided in the text of the conversation history to create a summary response. Separate different conversations into different points and return a message as a bulleted list of all the different topics/conversations. Pay extremely close attention to what messages are related to which conversations/topics and make sure to keep the summary of all messages relating to a certain topic/conversation under one bulletin point.\nWithin the messages, if there is ever a request or a question or an ask for anything, make sure to summarize it.\nIf there is nothing interesting or important, return 'Nothing important to summarize.'\nWhen returning the summary, include the link of the first message in a specific conversation/topic formatted like this after the summary:\nLink to conversation: 'hyperlink'.\nConversation history:" f"{conversation_data}",
        "provider": "openai_chat",
        "providerOptions": {
            "model": "gpt-3.5-turbo"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        return response.json()['data']['value']
    except:
        return "GoCaaS authorization failed"
