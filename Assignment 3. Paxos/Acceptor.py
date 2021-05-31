from Process import Process
from Message import Message
from MessageTypes import MessageTypes


class Acceptor(Process):
    def __init__(self, process_id):
        super().__init__(process_id)
        self.min_proposal = -1
        self.accepted_id = -1
        self.accepted_value = None


    def prepare(self, message):
        if message.source.process_id > self.accepted_id:
            self.accepted_id = message.source.process_id
            return Message(message.source, message.value, self, MessageTypes.PROMISE)


    def accept(self, message):
        if self.accepted_value is None:
            self.accepted_value = message.value
            return Message(message.source, message.value, message.destination, MessageTypes.ACCEPTED)


    def __str__(self):
        return f'A{self.process_id}'
