import os
import classFileOperations


class Logger:

    def __init__(self):
        # self.configuration = configuration
        pass


    def writeLog(self, directory, level, string, mode="a+"):
        # file = open(classFileOperations.FileOperations.join(directory, level + "_log.txt"), mode, newline="\r\n")
        # file.write(string + "\n")
        # file.close()
        classFileOperations.FileOperations.writeLineToFile(
            classFileOperations.FileOperations.join(directory, level + "_log.txt"), string, mode)
        #print(string)
