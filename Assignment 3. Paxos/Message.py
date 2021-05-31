from MessageTypes import MessageTypes


class Message:
    def __init__(self, destination, value, source, message_type):
        self.destination = destination
        self.value = value
        self.source = source
        self.message_type = message_type


    def get_args(self, message_type):
        if message_type == MessageTypes.PROPOSE: return f'v={self.value}'
        elif message_type == MessageTypes.PREPARE: return f'n={self.source.process_id}'
        elif message_type == MessageTypes.PROMISE: 
            prior = f"n={self.source.accepted_id}, v={self.source.accepted_value}" if self.source.accepted_value else None
            return f'n={self.destination.process_id} (Prior: {prior})'
        elif message_type == MessageTypes.ACCEPT: return f'n={self.source.process_id} v={self.value}'
        elif message_type == MessageTypes.ACCEPTED: return f'n={self.destination.process_id} v={self.value}'
        else: return ''    

    def __str__(self):
        return f'{self.message_type.value} {self.get_args(self.message_type)}'
