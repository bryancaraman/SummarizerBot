class Message:
    def __init__(self, text, link, user='Not specified'):
        self.message_data = {
            "text": text,
            "link": link,
            "user": user
        }

    
