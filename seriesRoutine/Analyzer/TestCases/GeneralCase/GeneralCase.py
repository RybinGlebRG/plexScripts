from seriesRoutine.Files import classFile, classFilesList
from seriesRoutine.Analyzer import ClassSeriesAnalyzer
from common import TestCase


def general_case():
    """
    This case tests multiple groups analysis.
    There are three groups with the same names but different paths.
    """

    def arrange():
        files = classFilesList.FilesList()
        for i in range(1, 4):
            files.add(classFile.File(str(i) + ".ac3", "/Lang/Sound/3"))
        for i in range(1, 4):
            files.add(classFile.File(str(i) + ".ac3", "/Lang/Sound/2"))
        for i in range(1, 4):
            files.add(classFile.File(str(i) + ".ac3", "/Lang/Sound/1"))
        return [files]

    def act(p_input):
        files = p_input[0]
        ClassSeriesAnalyzer.SeriesAnalyzer.setFileNumber(files)
        return [files]

    def check(p_input):
        files = p_input[0]
        for file in files:
            number = int(file.fileName[:1])
            if number != file.number:
                return False
        return True

    test_case = TestCase.TestCase(arrange, act, check)
    test_case.description = "SeriesAnalyzer General Case"

    return test_case
