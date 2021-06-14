from Simulation.Message.MessageTypes import MessageTypes


class Message:
    def __init__(self, source, destination, message_type):
        self.source = source
        self.destination = destination
        self.message_type = message_type


    def get_args(self, message_type):
        if message_type == MessageTypes.PROPOSE: return f'v={self.destination.value}'
        elif message_type == MessageTypes.PREPARE: return f'n={self.source.agent_id}'
        elif message_type == MessageTypes.PROMISE: 
            prior = f"n={self.source.agent_id}, v={self.source.value}" if self.source.value else None
            return f'n={self.destination.agent_id} (Prior: {prior})'
        elif message_type == MessageTypes.ACCEPT: return f'n={self.source.agent_id} v={self.source.value}'
        elif message_type == MessageTypes.ACCEPTED: return f'n={self.destination.agent_id} v={self.destination.value}'
        elif message_type == MessageTypes.REJECTED: return f'n={self.destination.agent_id}'
        else: return ''    


    def __str__(self):
        return f'{self.message_type.value} {self.get_args(self.message_type)}'


    @staticmethod
    def send_back(message, message_type):
        return Message(message.destination, message.source, message_type)
