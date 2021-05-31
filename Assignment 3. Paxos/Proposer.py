from Process import Process
from Message import Message
from MessageTypes import MessageTypes


class Proposer(Process):
    
    max_id = 0

    def __init__(self, name, process_id, value=None):
        super().__init__(name, process_id, value)
        self.suggested_value = value
        self.votes = 0
        self.majority = False
        self.consensus = False
        Proposer.max_id = max(Proposer.max_id, process_id + 1)


    def recieve_promise(self, message, majority):
        if message.source.value:
            self.value = max(self.value, message.source.value)

        self.votes += 1
        if self.votes >= majority and not self.majority:
            self.majority = True
            return lambda acceptor: Message(message.destination, acceptor, MessageTypes.ACCEPT)


    def recieve_fail(self):
        self.failed = True
        print(f'** {self} broke down **', end='')


    def recieve_repair(self):
        self.failed = False
        print(f'** {self} is repaired **', end='')


    def recieve_accepted(self, message):
        self.consensus = True


    def reset(self):
        self.votes = 0
        self.majority = False
        self.process_id = Proposer.max_id

    def __str__(self):
        return f'P{self.process_id}'
