from Simulation.Agents import Agent
from Simulation.Message import Message, MessageTypes


class Proposer(Agent):
    
    max_id = 0

    def __init__(self, name, agent_id, value=None):
        super().__init__(name, agent_id, value)
        self.votes = 0
        self.majority = False
        self.suggested_value = None
        self.consensus = False
        Proposer.max_id = max(Proposer.max_id, agent_id + 1)

    def recieve_promise(self, message, majority):
        if message.source.value:
            self.value = max(self.value, message.source.value)

        self.votes += 1
        if self.votes >= majority and not self.majority:
            self.majority = True
            return lambda acceptor: Message(message.destination, acceptor, MessageTypes.ACCEPT)

    def recieve_accepted(self, message):
        self.consensus = True

    def init_value(self, value):
        self.value = value
        self.suggested_value = value

    def reset(self):
        self.votes = 0
        self.majority = False
        self.agent_id = Proposer.max_id
