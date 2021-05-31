from MessageTypes import MessageTypes
from Message import Message
from Event import Event


def read_input_file():
    n_proposers, n_acceptors, max_ticks, events = 0, 0, 0, {}
    with open('input.txt', 'r') as file:
        n_proposers, n_acceptors, max_ticks = [int(value) for value in file.readline().split()]
        formatted_lines = file.read().splitlines()[:-1]
        for line in formatted_lines:
            event, tick = create_event(line)
            events[tick] = event
    return n_proposers, n_acceptors, max_ticks, events


def create_event(event_string):
    tick, message_type, *args = event_string.split()
    tick, message_type = int(tick), MessageTypes(message_type)
    event = event_map[message_type](tick, message_type, args)
    return event, tick


def propose(tick, message_type, args):
    args = [int(args[0]), int(args[1])]
    message = Message(*args, None, MessageTypes.PROPOSE)
    return Event(tick, [], [], message)


def fail(tick, message_type, args):
    fail_ids = [int(proposer_id) for proposer_id in args[1:]]
    message = Message(None, None, None, MessageTypes.FAIL)
    return Event(tick, fail_ids, [], message)


def recover(tick, message_type, args):
    recover_ids = [int(proposer_id) for proposer_id in args[1:]]
    message = Message(None, None, None, MessageTypes.RECOVER)
    return Event(tick, [], recover_ids, message)


event_map = { 
    MessageTypes.PROPOSE: propose,
    MessageTypes.FAIL: fail,
    MessageTypes.RECOVER: recover
}
