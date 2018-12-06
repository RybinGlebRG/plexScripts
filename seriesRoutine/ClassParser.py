import classFileOperations


class Parser:

    def __init__(self):
        pass

    def parse(self, file_name):
        key_value_dict = {}

        def getKeyFromString(line):
            key = ""
            foundDelimeter = False
            for letter in line:
                if letter != "=":
                    key += letter
                else:
                    foundDelimeter = True
                    break
            if not foundDelimeter:
                key = None
            return key.strip()

        def getValueFromString(line):
            def isMultipleValues(value):
                position = value.find(";")
                if position == -1:
                    return False
                else:
                    return True

            value = None
            delimiter = line.find("=")

            if delimiter != -1:
                if not isMultipleValues(line[(delimiter + 1):]):
                    value = line[(delimiter + 1):]
                    value = list(value.strip())
                else:
                    value = line[(delimiter + 1):]
                    value = value.split(";")
                    for i in range(0, len(value)):
                        value[i] = value[i].strip()
                if len(value) == 0:
                    value = None
            return value

        lines = classFileOperations.FileOperations.readFile(file_name)

        for line in lines:
            # print(line)
            if line[0] != "#":
                if getKeyFromString(line) is not None:
                    key_value_dict[getKeyFromString(line)] = getValueFromString(line)
        return key_value_dict