class AnalyzingGroup:

    def __init__(self, path):
        self.path = ""
        self.possibleNumbersList = []
        self.path = path
        self.files = []

    def append(self, file):
        self.files.append(file)
