class Answer:
    def __init__(self, type, content):
        self.type = type
        self.content = content


class AnswerType:
    CHOICE = "CHOICE"
    TEXT = "TEXT"
    MATCHING = "MATCHING"
