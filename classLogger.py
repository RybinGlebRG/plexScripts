import os
import classFileOperations


class Logger:

    def __init__(self):
        # self.configuration = configuration
        pass

    def isLevelAcceptable(self, level):
        return True
        # #print(self.configuration.getValueAsList("logLevels"))
        # if not self.configuration.isIncludes("logLevels", level):
        #     return False
        # loggerLevel = self.configuration.getValue("loggerLevel")
        # levelOrder = 0
        # loggerLevelOrder = 0
        # counter = 0
        # for lvl in self.configuration.getValueAsList("logLevels"):
        #     if lvl == level:
        #         levelOrder = self.configuration.getValueAsList("logLevelsOrder")[counter]
        #     if lvl == loggerLevel:
        #         loggerLevelOrder = self.configuration.getValueAsList("logLevelsOrder")[counter]
        #     counter += 1
        # #print(levelOrder)
        # #print(loggerLevelOrder)
        # if levelOrder > loggerLevelOrder:
        #     return False
        # return True

    def writeLog(self, directory, level, string, mode="a+"):
        if self.isLevelAcceptable(level):
            # file = open(classFileOperations.FileOperations.join(directory, level + "_log.txt"), mode, newline="\r\n")
            # file.write(string + "\n")
            # file.close()
            classFileOperations.FileOperations.writeLineToFile(
                classFileOperations.FileOperations.join(directory, level + "_log.txt"), string, mode)
