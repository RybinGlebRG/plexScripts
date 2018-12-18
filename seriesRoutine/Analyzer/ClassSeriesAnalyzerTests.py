from seriesRoutine.Files import classFile, classFilesList
from seriesRoutine.Analyzer import ClassSeriesAnalyzer
from seriesRoutine.Analyzer.TestCases.GeneralCase import GeneralCase


class AnalyzerTests:

    def __init__(self):
        self.cases = []

    def run(self):
        self.cases.append(GeneralCase.general_case())

        for test_case in self.cases:
            test_case.run()
            if test_case.result is False:
                print(test_case.description + ": Failed")
                return False
            else:
                print(test_case.description + ": Passed")
                return True
