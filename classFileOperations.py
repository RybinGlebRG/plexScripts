import io
import os
import shutil


class FileOperations:

    @staticmethod
    def open(fileName):
        file = io.open(fileName, encoding="utf-8-sig", errors="surrogateescape")
        return file

    @staticmethod
    def rename(oldName, newName):
        os.rename(oldName, newName)

    @staticmethod
    def walk(directory):
        lst = []
        # print(directory.rstrip().encode("utf-8"))
        for root, dirs, files in os.walk(directory):
            # print("root:" + str(root))
            # print("files:"+str(files))
            lst.append([root, dirs, files])
        return lst

    @staticmethod
    def rmtree(directory):
        shutil.rmtree(directory)

    @staticmethod
    def makedirs(directory):
        os.makedirs(directory)

    @staticmethod
    def join(path1, path2):
        # print("---------------------")
        # print("join:")
        # print(path1)
        # print(path2)
        # print("---------------------")
        return os.path.join(path1, path2)

    @staticmethod
    def symlink(src, dst):
        os.symlink(src, dst)

    @staticmethod
    def osName():
        return os.name

    @staticmethod
    def exists(path):
        return os.path.exists(path)

    @staticmethod
    def isfile(path):
        return os.path.isfile(path)

    @staticmethod
    def listdir(path):
        lst = []
        files = os.listdir(path)
        for file in files:
            lst.append(file)
        return lst

    @staticmethod
    def dirname(path):
        # print(path)
        return os.path.dirname(path)

    @staticmethod
    def abspath(path):
        # print(path)
        return os.path.abspath(path)

    @staticmethod
    def readFile(path):
        # print(path)
        lines = []
        file = FileOperations.open(path)
        for line in file:
            lines.append(line)

        return lines

    @staticmethod
    def writeLineToFile(file, line):
        # print(line)
        # print(repr(line))
        # file = io.open(path, mode=mode, newline="\r\n", encoding="utf-8", errors="surrogateescape")
        file.write(line + "\n")
        # file.close()

    @staticmethod
    def open_file(path, mode="a+"):
        file = io.open(path, mode=mode, newline="\r\n", encoding="utf-8", errors="surrogateescape")
        return file

    @staticmethod
    def close_file(file):
        file.close()
