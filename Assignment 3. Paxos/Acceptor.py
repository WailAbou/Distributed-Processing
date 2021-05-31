from Process import Process
from Message import Message
from MessageTypes import MessageTypes


class Acceptor(Process):
    def __init__(self, process_id):
        super().__init__(process_id)
        self.max_id = -1
        self.accepted_messsage = None


    def prepare(self, message):
        if message.source.process_id > self.max_id:
            self.max_id = message.source.process_id
            return Message(message.source, self.accepted_messsage.value if self.accepted_messsage else message.value, self, MessageTypes.PROMISE)


    def accept(self, message):
        if message.source.process_id == self.max_id:
            self.accepted_messsage = message
            return Message(message.source, message.value, message.destination, MessageTypes.ACCEPTED)
        else:
            return Message(message.source, message.value, message.destination, MessageTypes.REJECTED)


    def __str__(self):
        return f'A{self.process_id}'
