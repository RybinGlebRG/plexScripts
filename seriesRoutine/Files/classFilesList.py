import classFileOperations
from seriesRoutine.Files import classFile


class FilesList:

    def __init__(self):
        self.filesList = []

    def __eq__(self, other):
        if self.filesList != other.filesList:
            return False
        return True

    def __ne__(self, other):
        if self.filesList != other.filesList:
            return True
        return False

    def __getitem__(self, key):
        return self.filesList[key]

    def __iter__(self):
        return iter(self.filesList)

    def get_list(self):
        return self.filesList

    def add(self, file):
        self.filesList.append(file)

    def filter_by_number(self, number):
        filtered = FilesList()
        # Should not filter by number if there is no number
        if number is None:
            return filtered
        for file in self.filesList:
            if file.number == number:
                filtered.add(file)
        return filtered

    def filter_by_suffixes(self, suffixes):
        filtered = FilesList()
        # Should not filter by suffixes if there are no suffixes
        if suffixes is None:
            return filtered
        for file in self.filesList:
            if file.getSuffix() in suffixes:
                filtered.add(file)
        return filtered

    def load(self, directoryPath, configuration):
        # def getSourcePath(directoryPath, configuration):
        #     folders = []
        #     for folderList in classFileOperations.FileOperations.walk(directoryPath):
        #         folders = folderList[1]
        #         break
        #     sourcePath = directoryPath
        #     for folder in folders:
        #         if configuration.isIncludes("sourcePossibleLocation", folder):
        #             sourcePath = classFileOperations.FileOperations.join(directoryPath, folder)
        #             if configuration.getValue("linkAudio")[0] == "A":
        #                 configuration.setValue("linkAudio", "N")
        #             if configuration.getValue("linkSubs")[0] == "A":
        #                 configuration.setValue("linkSubs", "N")
        #             break
        #     return sourcePath

        langPath = classFileOperations.FileOperations.join(directoryPath, configuration.getValue("langPath")[0])
        sourcePath = configuration.getValue("source_path")

        for file in classFileOperations.FileOperations.listdir(sourcePath):
            if classFileOperations.FileOperations.isfile(classFileOperations.FileOperations.join(sourcePath, file)):
                new_file = classFile.File(file, sourcePath)
                new_file.check_specified(configuration)
                self.add(new_file)

        for vector in classFileOperations.FileOperations.walk(langPath):
            for file in vector[2]:
                new_file = classFile.File(file, vector[0])
                new_file.check_specified(configuration)
                self.add(new_file)

    def load_v2(self, directory, suffixes, configuration, is_recursive=True):
        for vector in classFileOperations.FileOperations.walk(directory):
            for file in vector[2]:
                new_file = classFile.File(file, vector[0])
                if new_file.getSuffix() in suffixes:
                    new_file.check_specified(configuration)
                    self.add(new_file)
            if not is_recursive:
                break

    def clear(self):
        self.filesList.clear()
