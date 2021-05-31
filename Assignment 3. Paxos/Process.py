class Process:
    def __init__(self, name, process_id, value):
        self.name = name
        self.process_id = process_id
        self.value = value
        self.start_id = process_id
        self.failed = False


    def __str__(self):
        return self.name + self.start_id
