from Simulation.Agents import Proposer, Acceptor
from Simulation.Network import Network
from Simulation.Message import MessageTypes
from Inputs import read_input


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
                [agent.recieve_fail() for agent in event.fails]
            elif message.message_type == MessageTypes.RECOVER:
                [agent.recieve_repair() for agent in event.repairs]
        else:
            message = network.extract_message()
            if message is not None:
                network.deliver_messsage(message)

    print()
    for proposer in proposers.values():
        if proposer.consensus:
            print(f'\n{proposer} has reached consensus (suggested: {proposer.suggested_value}, accepted: {proposer.value})', end='')


if __name__ == "__main__":
    input_variables = read_input('Inputs/advanced.txt')
    simulate(*input_variables)
