class AnalyzingGroup:

    def __init__(self, path):
        self.path = path
        self.files = []
        self.hypothesis = -1

    def append(self, file):
        self.files.append(file)
