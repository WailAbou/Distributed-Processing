from Proposer import Proposer
from Acceptor import Acceptor
from Network import Network
from MessageTypes import MessageTypes
from Input import read_input_file, proposers, acceptors


def simulate(n_proposers, n_acceptors, max_ticks, events):
    global proposers, acceptors
    
    for p_id in range(1, n_proposers + 1):
        if p_id not in proposers:
            proposers[p_id] = Proposer('P', p_id)

    for a_id in range(1, n_acceptors + 1):
        if a_id not in acceptors:
            acceptors[a_id] = Acceptor('A', a_id)

    network = Network(proposers, acceptors)

    for i in range(max_ticks):
        if len(events) == 0 and len(network.queue) == 0:
            break

        print(f'\n{str(i).zfill(3)}: ', end='')
        event = events.get(i)
        if event is not None:
            events.pop(i)
            message = event.message
            if message.message_type == MessageTypes.PROPOSE:
                network.deliver_messsage(message)
            elif message.message_type == MessageTypes.FAIL:
                [proposers[proposer_id].recieve_fail() for proposer_id in event.fails]
            elif message.message_type == MessageTypes.RECOVER:
                [proposers[proposer_id].recieve_repair() for proposer_id in event.repairs]
        else:
            message = network.extract_message()
            if message is not None:
                network.deliver_messsage(message)

    print()
    for proposer in proposers.values():
        if proposer.consensus:
            print(f'\n{proposer} has reached consensus (suggested: {proposer.suggested_value}, accepted: {proposer.value})', end='')


if __name__ == "__main__":
    input_variables = read_input_file()
    simulate(*input_variables)
