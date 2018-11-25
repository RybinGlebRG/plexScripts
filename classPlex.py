import requests
import json
import xml.etree.ElementTree as ET


class Plex:

    def __init__(self,configuration):
        self.configuration = configuration
        self.plexUser=self.configuration.getValue("plexUser")
        self.plexPass=self.configuration.getValue("plexPass")
        self.plexIPAddress=self.configuration.getValue("plexIPAddress")
        self.plexPort=self.configuration.getValue("plexPort")
        self.authToken = self.getAuthToken()

    def getAuthToken(self):
        headers = {"X-Plex-Client-Identifier": "TEST", "X-Plex-Product": "REFRESH_SCRIPT",
                   "X-Plex-Version": "1.0.0"}
        data = "user%5Blogin%5D=" + self.plexUser + "&user%5Bpassword%5D=" + self.plexPass
        response = requests.post("https://plex.tv/users/sign_in.json", headers=headers, data=data)
        # print(response.text)
        authToken = json.loads(response.text)["user"]["authToken"]
        return authToken

    def getLibraryKey(self,plexLibrary):
        response = requests.get(
            "http://" + self.plexIPAddress + ":" + self.plexPort + "/library/sections/?X-Plex-Token=" + self.authToken)
        # print(response.text)
        root = ET.fromstring(response.text)
        libraryKey = ""
        for child in root.findall("Directory"):
            # print(child.attrib)
            if child.attrib["title"] == plexLibrary:
                libraryKey = child.attrib["key"]
                break
        return libraryKey

    def refershLibrary(self,plexLibrary):

      # print(authToken)
        libraryKey=self.getLibraryKey(plexLibrary)
        #print(libraryKey)
        response=requests.get("http://"+self.plexIPAddress+":"+self.plexPort+"/library/sections/"+libraryKey+"/refresh?X-Plex-Token=" + self.authToken)
        #print(response)