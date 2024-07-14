class Message:
    def __init__(self, text, ts, user='Not specified'):
        self.message_data = {
            "text": text,
            "ts": ts,
            "user": user
        }

    
