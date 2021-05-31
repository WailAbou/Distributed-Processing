class Process:
    def __init__(self, name, process_id, value):
        self.name = name
        self.process_id = process_id
        self.value = value
        self.start_id = process_id
        self.failed = False

    def recieve_fail(self):
        self.failed = True
        print(f'** {self} broke down **', end='')

    def recieve_repair(self):
        self.failed = False
        print(f'** {self} is repaired **', end='')

    def __str__(self):
        return f'{self.name}{self.start_id}'
