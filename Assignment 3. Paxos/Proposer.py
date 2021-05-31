from Process import Process
from Message import Message
from MessageTypes import MessageTypes


class Proposer(Process):
    def __init__(self, process_id):
        super().__init__(process_id)
        self.suggested_value = None
        self.accepted_value = None
        self.votes = 0
        self.majority = False
        self.consensus = False


    def promise(self, message, majority):
        self.votes += 1
        if self.votes >= majority and self.majority == False:
            self.majority = True
            return lambda acceptor: Message(acceptor, message.value, message.destination, MessageTypes.ACCEPT)


    def fail(self):
        self.failed = True
        print(f'** {self} broke down **', end='')


    def repair(self):
        self.failed = False
        print(f'** {self} is repaired **', end='')


    def accepted(self, message):
        self.consensus = True
        self.accepted_value = message.value


    def __str__(self):
        return f'P{self.process_id}'
