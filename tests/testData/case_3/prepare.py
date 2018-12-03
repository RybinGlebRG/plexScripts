import classFileOperations

def prepare():
    path = classFileOperations.FileOperations.abspath(__file__)
    dir = classFileOperations.FileOperations.dirname(path)
    oldname = classFileOperations.FileOperations.join(dir, "Some serial")
    oldname = classFileOperations.FileOperations.join(oldname, "configuration.txt")
    newname = classFileOperations.FileOperations.join(dir, "Some serial")
    newname = classFileOperations.FileOperations.join(newname, "configuration.ready")
    if classFileOperations.FileOperations.exists(oldname):
        classFileOperations.FileOperations.rename(oldname, newname)
