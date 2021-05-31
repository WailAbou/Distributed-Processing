from Process import Process
from Message import Message
from MessageTypes import MessageTypes


class Acceptor(Process):
    def __init__(self, name, process_id, value=None):
        super().__init__(name, process_id, value)
        self.max_id = -1


    def recieve_prepare(self, message):
        if message.source.process_id > self.max_id:
            self.max_id = message.source.process_id
            return Message.send_back(message, MessageTypes.PROMISE)


    def recieve_accept(self, message):
        if message.source.process_id == self.max_id:
            self.value = message.source.value
            return Message.send_back(message, MessageTypes.ACCEPTED)
        else:
            return Message.send_back(message, MessageTypes.REJECTED)


    def __str__(self):
        return f'A{self.process_id}'
