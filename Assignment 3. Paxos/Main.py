from Proposer import Proposer
from Acceptor import Acceptor
from Network import Network
from MessageTypes import MessageTypes
from Input import read_input_file


def simulate(proposers, acceptors, max_ticks, events):
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
                [process.recieve_fail() for process in event.fails]
            elif message.message_type == MessageTypes.RECOVER:
                [process.recieve_repair() for process in event.repairs]
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
