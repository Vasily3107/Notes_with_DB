class Note:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __iter__(self):
        yield self.name
        yield self.text

    def __repr__(self):
        return f"NAME: {self.name:20} TEXT: {self.text}"
