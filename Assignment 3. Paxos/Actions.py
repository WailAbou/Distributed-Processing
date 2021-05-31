from MessageTypes import MessageTypes
from Message import Message
from math import ceil


accepted_value = 0


def propose(network, message):
    new_message = lambda acceptor: Message(acceptor, message.value, message.destination, MessageTypes.PREPARE)
    [network.queue_message(new_message(acceptor)) for acceptor in network.acceptors.values()]


def prepare(network, message):
    global accepted_value
    message.value = max(accepted_value, message.value)
    new_message = message.destination.prepare(message)
    accepted_value = max(new_message.value, message.value)
    network.queue_message(new_message)


def promise(network, message):
    majority = ceil(len(network.acceptors) / 2)
    new_message = message.destination.promise(message, majority)
    if new_message != None:
        [network.queue_message(new_message(acceptor)) for acceptor in network.acceptors.values()]


def accept(network, message):
    new_message = message.destination.accept(message)
    network.queue_message(new_message)


def accepted(network, message):
    message.destination.accepted(message)


def rejected(network, message):
    new_message = Message(message.source, message.value, message.destination, MessageTypes.PREPARE)
    network.queue_message(new_message)


action_map = { 
    MessageTypes.PROPOSE: propose,
    MessageTypes.PREPARE: prepare,
    MessageTypes.PROMISE: promise,
    MessageTypes.ACCEPT: accept,
    MessageTypes.ACCEPTED: accepted,
    MessageTypes.REJECTED: rejected
}
