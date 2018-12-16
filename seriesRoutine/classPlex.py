import requests
import json
import xml.etree.ElementTree as ET


class Plex:

    def __init__(self, configuration):
        self.configuration = configuration
        self.plexUser = self.configuration.getValue("plexUser")[0]
        self.plexPass = self.configuration.getValue("plexPass")[0]
        self.plexIPAddress = self.configuration.getValue("plexIPAddress")[0]
        self.plexPort = self.configuration.getValue("plexPort")[0]
        self.authToken = self.getAuthToken()

    def getAuthToken(self):
        headers = {"X-Plex-Client-Identifier": "TEST", "X-Plex-Product": "REFRESH_SCRIPT",
                   "X-Plex-Version": "1.0.0"}
        data = "user%5Blogin%5D=" + self.plexUser + "&user%5Bpassword%5D=" + self.plexPass
        response = requests.post("https://plex.tv/users/sign_in.json", headers=headers, data=data)
        # print(response.text)
        authToken = json.loads(response.text)["user"]["authToken"]
        return authToken

    def getLibraryKey(self, plexLibrary):
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

    def refresh_library(self, plex_library):
        is_successful = False
        cnt = 0
        while not is_successful:
            try:
                library_key = self.getLibraryKey(plex_library)
                requests.get(
                    "http://" + self.plexIPAddress + ":" + self.plexPort + "/library/sections/" + library_key +
                    "/refresh?X-Plex-Token=" + self.authToken)

                is_successful = True
            except Exception as e:
                cnt += 1
                if cnt == 10:
                    raise Exception(str(e))

        # # print(authToken)
        # libraryKey = self.getLibraryKey(plexLibrary)
        # # print(libraryKey)
        # response = requests.get(
        #     "http://" + self.plexIPAddress + ":" + self.plexPort + "/library/sections/" + libraryKey + "/refresh?X-Plex-Token=" + self.authToken)
        # # print(response)
