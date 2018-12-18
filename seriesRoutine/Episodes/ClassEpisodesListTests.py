from seriesRoutine.Episodes import ClassEpisodesList
from seriesRoutine.Files import classFile, classFilesList
from common import TestCase
from seriesRoutine.Episodes.TestCases.GeneralCase import GeneralCase
from seriesRoutine.Episodes.TestCases.BleachCase import BleachCase


class EpisodesTests:

    def __init__(self):
        self.cases = []

    def run(self):
        self.cases.append(GeneralCase.general_case())
        self.cases.append(BleachCase.bleach_case())

        for test_case in self.cases:
            test_case.run()
            if test_case.result is False:
                print(test_case.description + ": Failed")
                return False
            else:
                print(test_case.description + ": Passed")
                return True
