from Actions import action_map


class Network:
    def __init__(self, proposers, acceptors):
        self.queue = []
        self.proposers = proposers
        self.acceptors = acceptors


    def queue_message(self, message):
        self.queue.append(message)


    def extract_message(self):
        valid_message = None
        for message in self.queue:
            if not message.destination.failed and not message.source.failed:
                valid_message = message
                self.queue.remove(message)
                break
        return valid_message


    def deliver_messsage(self, message):
        print(f'{message.source} -> {message.destination} {message}', end='')
        action_map[message.message_type](self, message)
