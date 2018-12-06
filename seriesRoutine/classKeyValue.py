class KeyValue:

    def __init__(self, key, value=""):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if self.key != other.key:
            return False
        if self.value != other.value:
            return False
        return True

    def __ne__(self, other):
        if self.key != other.key:
            return True
        if self.value != other.value:
            return True
        return False

    def getKey(self):
        return self.key

    def setKey(self, value):
        self.key = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
