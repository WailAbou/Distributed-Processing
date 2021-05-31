from Proposer import Proposer
from MessageTypes import MessageTypes
from Message import Message
from math import ceil


once = False

def propose(network, message):
    prepare_message = lambda acceptor: Message(message.destination, acceptor, MessageTypes.PREPARE)
    [network.queue_message(prepare_message(acceptor)) for acceptor in network.acceptors.values()]


def prepare(network, message):
    promise_message = message.destination.recieve_prepare(message)
    network.queue_message(promise_message)


def promise(network, message):
    majority = ceil(len(network.acceptors) / 2)
    accept_message = message.destination.recieve_promise(message, majority)
    if accept_message is not None:
        [network.queue_message(accept_message(acceptor)) for acceptor in network.acceptors.values()]


def accept(network, message):
    accepted_or_rejected_message = message.destination.recieve_accept(message)
    network.queue_message(accepted_or_rejected_message)


def accepted(network, message):
    message.destination.recieve_accepted(message)


def rejected(network, message):
    global once
    if not once:
        once = True
        message.destination.votes = 0
        message.destination.majority = False
        message.destination.process_id = Proposer.max_id
        propose(network, message)
        # prepare_message = Message.send_back(message, MessageTypes.PREPARE)
        # network.queue_message(prepare_message)


send_message = { 
    MessageTypes.PROPOSE: propose,
    MessageTypes.PREPARE: prepare,
    MessageTypes.PROMISE: promise,
    MessageTypes.ACCEPT: accept,
    MessageTypes.ACCEPTED: accepted,
    MessageTypes.REJECTED: rejected
}
