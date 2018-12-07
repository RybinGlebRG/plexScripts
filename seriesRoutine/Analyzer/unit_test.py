from seriesRoutine import classFilesList, classFile
from seriesRoutine.Analyzer import classSeriesAnalyzer


def case_1():
    """
    This case tests multiple groups analysis.
    There are three groups with the same names but different paths.
    """
    files = classFilesList.FilesList()
    for i in range(1, 4):
        files.add(classFile.File(str(i) + ".ac3", "/Lang/Sound/3"))
    for i in range(1, 4):
        files.add(classFile.File(str(i) + ".ac3", "/Lang/Sound/2"))
    for i in range(1, 4):
        files.add(classFile.File(str(i) + ".ac3", "/Lang/Sound/1"))

    classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(files)

    for file in files:
        number = int(file.fileName[:1])
        if number != file.number:
            return False
    return True


def run():
    result = True
    result = result and case_1()
    return result
