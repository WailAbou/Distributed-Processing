from enum import Enum

class MessageTypes(Enum):
    PROPOSE = 'PROPOSE'
    PREPARE = 'PREPARE'
    PROMISE = 'PROMISE'
    ACCEPT = 'ACCEPT'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    FAIL = 'FAIL'
    RECOVER = 'RECOVER'
