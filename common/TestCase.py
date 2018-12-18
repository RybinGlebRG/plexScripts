class TestCase:

    def __init__(self, arrange, act, check):
        self.arrange = arrange
        self.act = act
        self.check = check
        self.result = None
        self.description = None

    def run(self):
        self.result = self.check(self.act(self.arrange()))
