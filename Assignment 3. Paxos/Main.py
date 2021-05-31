from Proposer import Proposer
from Acceptor import Acceptor
from Network import Network
from MessageTypes import MessageTypes
from Input import read_input_file


def simulate(n_proposers, n_acceptors, max_ticks, events):
    proposers = { pId + 1: Proposer(pId + 1) for pId in range(n_proposers) }
    acceptors = { aId + 1: Acceptor(aId + 1) for aId in range(n_acceptors) }
    network = Network(proposers, acceptors)

    for i in range(max_ticks):
        if len(events) == 0 and len(network.queue) == 0:
            break

        print(f'\n{str(i).zfill(3)}: ', end='')
        event = events.get(i)
        if event is not None:
            events.pop(i)
            if event.message.message_type == MessageTypes.PROPOSE:
                proposers[event.message.destination].suggested_value = event.message.value
                event.message.destination = proposers[event.message.destination]
                network.deliver_messsage(event.message)
            elif event.message.message_type == MessageTypes.FAIL:
                [proposers[proposer_id].fail() for proposer_id in event.fails]
            elif event.message.message_type == MessageTypes.RECOVER:
                [proposers[proposer_id].repair() for proposer_id in event.repairs]
        else:
            message = network.extract_message()
            if message is not None:
                network.deliver_messsage(message)

    print()
    for proposer in proposers.values():
        if proposer.consensus:
            print(f'\n{proposer} has reached consensus (suggested: {proposer.accepted_value}, accepted: {proposer.accepted_value})', end='')


if __name__ == "__main__":
    input_variables = read_input_file()
    simulate(*input_variables)
