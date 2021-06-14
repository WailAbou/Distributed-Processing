from Simulation.Network.Actions import send_message


class Network:
    def __init__(self, proposers, acceptors):
        self.queue = []
        self.proposers = proposers
        self.acceptors = acceptors


    def queue_message(self, message):
        self.queue.append(message)


    def extract_message(self):
        for message in self.queue:
            if not message.destination.failed and not message.source.failed:
                self.queue.remove(message)
                return message


    def deliver_messsage(self, message):
        print(f'{message.source} -> {message.destination} {message}', end='')
        send_message[message.message_type](self, message)
