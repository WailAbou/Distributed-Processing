from Simulation.Agents import Proposer, Acceptor
from Simulation.Message import Message, MessageTypes
from Simulation.Network import Event


proposers, acceptors = {}, {}


def read_input(file_path):
    global proposers, acceptors
    n_proposers, n_acceptors, max_ticks, events = 0, 0, 0, {}

    with open(file_path, 'r') as file:
        n_proposers, n_acceptors, max_ticks = [int(value) for value in file.readline().split()]
        proposers = { p_id: Proposer('P', p_id) for p_id in range(1, n_proposers + 1) }
        acceptors = { a_id: Acceptor('A', a_id) for a_id in range(1, n_acceptors + 1) }
        formatted_lines = file.read().splitlines()[:-1]
        for line in formatted_lines:
            event, tick = create_event(line)
            events[tick] = event
    
    return proposers, acceptors, max_ticks, events


def create_event(event_string):
    tick, message_type, *args = event_string.split()
    tick, message_type = int(tick), MessageTypes(message_type)
    event = event_map[message_type](tick, message_type, args)
    return event, tick


def propose(tick, message_type, args):
    proposer_id, proposer_value = [int(args[0]), int(args[1])]
    proposers[proposer_id].init_value(proposer_value)
    message = Message(None, proposers[proposer_id], MessageTypes.PROPOSE)
    return Event(tick, [], [], message)


def fail(tick, message_type, args):
    fail_agentes = get_agentes(args)
    message = Message(None, None, MessageTypes.FAIL)
    return Event(tick, fail_agentes, [], message)


def recover(tick, message_type, args):
    recover_agentes = get_agentes(args)
    message = Message(None, None, MessageTypes.RECOVER)
    return Event(tick, [], recover_agentes, message)


def get_agentes(args):
    agent_type, agent_ids = args[0], [int(agent_id) for agent_id in args[1:]]
    if agent_type == 'PROPOSER':
        return [proposers[proposer_id] for proposer_id in proposers if proposer_id in agent_ids]
    elif agent_type == 'ACCEPTOR':
        return [acceptors[acceptor_id] for acceptor_id in acceptors if acceptor_id in agent_ids]


event_map = { 
    MessageTypes.PROPOSE: propose,
    MessageTypes.FAIL: fail,
    MessageTypes.RECOVER: recover
}
