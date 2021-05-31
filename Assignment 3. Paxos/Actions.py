from MessageTypes import MessageTypes
from Message import Message
from math import ceil


def propose(network, message):
    for acceptor in network.acceptors.values():
        new_message = Message(acceptor, message.value, message.destination, MessageTypes.PREPARE)
        network.queue_message(new_message)


def prepare(network, message):
    new_message = message.destination.prepare(message)
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


action_map = { 
    MessageTypes.PROPOSE: propose,
    MessageTypes.PREPARE: prepare,
    MessageTypes.PROMISE: promise,
    MessageTypes.ACCEPT: accept,
    MessageTypes.ACCEPTED: accepted
}
