import os
import classFileOperations


class Watcher:

    def __init__(self, configuration):
        self.configuration = configuration
        self.watcherPath = configuration.getValue("watcherPath")

    def watchForFile(self, fileName):
        foundDirectory = ""
        foundFile = ""
        #print(("self.watcherPath:"+self.watcherPath).encode("utf-8"))
        for root, dirs, files in classFileOperations.FileOperations.walk(self.watcherPath):
            #print(files)
            for file in files:
                #print(classFileOperations.FileOperations.join(root, file))
                #print(classFileOperations.FileOperations.join(root, fileName))
                #print(file)
                #print(fileName)
                if file == fileName:
                    #print("LOL")
                    foundDirectory = root
                    foundFile = file
                    break
        return foundDirectory, foundFile
