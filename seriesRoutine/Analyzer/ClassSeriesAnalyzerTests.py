from seriesRoutine.Files import classFile, classFilesList
from seriesRoutine.Analyzer import ClassSeriesAnalyzer


class AnalyzerTests:

    def __init__(self):
        self.cases = []

    def case_1(self):
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
            return files

        def act(files):
            ClassSeriesAnalyzer.SeriesAnalyzer.setFileNumber(files)

        def check(files):
            for file in files:
                number = int(file.fileName[:1])
                if number != file.number:
                    return False
            return True

        files = arrange()
        act(files)
        result = check(files)

        return result

    def run(self):
        self.cases.append(self.case_1)

        for case in self.cases:
            if not case():
                return False
        return True
