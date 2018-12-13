class FilesListTests:

    def __init__(self):
        self.cases = []

    def case_1(self):
        """
        This case tests load function
        """
        raise NotImplementedError

    def run(self):
        self.cases.append(self.case_1)

        for case in self.cases:
            if not case():
                return False
        return True
