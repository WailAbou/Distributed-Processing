from Simulation.Agents import Agent
from Simulation.Message import Message, MessageTypes


class Acceptor(Agent):
    def __init__(self, name, agent_id, value=None):
        super().__init__(name, agent_id, value)
        self.max_id = -1


    def recieve_prepare(self, message):
        if message.source.agent_id > self.max_id:
            self.max_id = message.source.agent_id
            return Message.send_back(message, MessageTypes.PROMISE)


    def recieve_accept(self, message):
        if message.source.agent_id == self.max_id:
            self.value = message.source.value
            return Message.send_back(message, MessageTypes.ACCEPTED)
        else:
            return Message.send_back(message, MessageTypes.REJECTED)
