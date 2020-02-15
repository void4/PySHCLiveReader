import json

class Data:
    def __init__(self, title, items):
        self.title = title
        self.dataset = items

    def __repr__(self):
        if self.dataset["Name"]["Value"] == "":
            return ""

        s = f'"{self.title}":\n'
        s += "{\n"
        for key, value in self.dataset.items():
            rawData = value["Value"]
            s += f"\t{key}: {str(rawData)},\n"

        s = s[:-2]
        s += "\n}"
        return s

def CreateValueDictionary(addr, size):
    return {
        "Address": addr,
        "Value": 0,
        "Size": size
    }

def CreatePlayerDataDictionary(name, gold, units, popularity, population, housing):
    return {
        "Name": CreateValueDictionary(name, 32),
        "Gold": CreateValueDictionary(gold, 4),
        "Units": CreateValueDictionary(units, 4),
        "Popularity": CreateValueDictionary(popularity, 4),
        "Population": CreateValueDictionary(population, 2),
        "Housing": CreateValueDictionary(housing, 2)
    }

def CreateLeaderBoardDictionary(name, gold, units, food, stone, iron, wood, buildings, razed, population, active):
    return {
        "Name": CreateValueDictionary(name, 32),
        "Total Gold": CreateValueDictionary(gold, 4),
        "Troops Produced": CreateValueDictionary(units, 4),
        "Food Produced": CreateValueDictionary(food, 4),
        "Stone Produced": CreateValueDictionary(stone, 4),
        "Iron Produced": CreateValueDictionary(iron, 4),
        "Wood Produced": CreateValueDictionary(wood, 4),
        "Buildings Lost": CreateValueDictionary(buildings, 4),
        "Enemy Building Destroyed": CreateValueDictionary(razed, 4),
        "Highest Population": CreateValueDictionary(population, 2),
        "Housing": CreateValueDictionary(active, 2)
    }

class MemoryMap:
    def __init__(self):
        self.playerdata = {
            "Player1": Data("Player1", CreatePlayerDataDictionary(0x024BA286,0x011F2938,0x011F27E4,0x011F2870,0x011F45AC,0x011F24A0)),
            "Player2": Data("Player2", CreatePlayerDataDictionary(0x024BA2E0,0x011F632C,0x011F61D8,0x011F6264,0x011F7FA0,0x011F5E94)),
            "Player3": Data("Player3", CreatePlayerDataDictionary(0x024BA33A,0x011F9D20,0x011F9BCC,0x011F9C58,0x011FB994,0x011F9888)),
            "Player4": Data("Player4", CreatePlayerDataDictionary(0x024BA394,0x011FD714,0x011FD5C0,0x011FD64C,0x011FF388,0x011FD27C)),
            "Player5": Data("Player5", CreatePlayerDataDictionary(0x024BA3EE,0x01201108,0x01200fb4,0x01201040,0x01202D7C,0x01200C70)),
            "Player6": Data("Player6", CreatePlayerDataDictionary(0x024BA448,0x01204AFC,0x012049A8,0x01204A34,0x01206770,0x01204664)),
            "Player7": Data("Player7", CreatePlayerDataDictionary(0x024BA4A2,0x012084F0,0x0120839C,0x01208428,0x0120A164,0x01208058)),
            "Player8": Data("Player8", CreatePlayerDataDictionary(0x024BA4FC,0x0120BEE4,0x0120BD90,0x0120BE1C,0x0120DB58,0x120BA4C))
        }
        self.leaderboard = {
            "Player1": Data("Player1", CreateLeaderBoardDictionary(0x024BA286,0x024BA564, 0x024BA888, 0x024BA730, 0x024BA778, 0x024BA754, 0x024BA79C, 0x024BA81C, 0x024BA70C, 0x024BA586, 0x011F24A0)),
            "Player2": Data("Player2", CreateLeaderBoardDictionary(0x024BA2E0, 0x024BA568, 0x024BA88C, 0x024BA734, 0x024BA77C, 0x024BA758, 0x024BA7A0, 0x024BA820, 0x024BA710, 0x024BA588, 0x011F5E94)),
            "Player3": Data("Player3", CreateLeaderBoardDictionary(0x024BA33A, 0x024BA56C, 0x024BA890, 0x024BA738, 0x024BA780, 0x024BA75C, 0x024BA7A4, 0x024BA824, 0x024BA714, 0x024BA58A, 0x011F9888)),
            "Player4": Data("Player4", CreateLeaderBoardDictionary(0x024BA394, 0x024BA570, 0x024BA894, 0x024BA73C, 0x024BA784, 0x024BA760, 0x024BA7A8, 0x024BA828, 0x024BA718, 0x024BA58C, 0x011FD27C)),
            "Player5": Data("Player5", CreateLeaderBoardDictionary(0x024BA448, 0x024BA574, 0x024BA898, 0x024BA740, 0x024BA788, 0x024BA764, 0x024BA7AC, 0x024BA82C, 0x024BA71C, 0x024BA58E, 0x01200C70)),
            "Player6": Data("Player6", CreateLeaderBoardDictionary(0x024BA448, 0x024BA578, 0x024BA89C, 0x024BA744, 0x024BA78C, 0x024BA768, 0x024BA7B0, 0x024BA830, 0x024BA720, 0x024BA590, 0x01204664)),
            "Player7": Data("Player7", CreateLeaderBoardDictionary(0x024BA4A2, 0x024BA57C, 0x024BA8A0, 0x024BA748, 0x024BA790, 0x024BA76C, 0x024BA7B4, 0x024BA834, 0x024BA724, 0x024BA592, 0x01208058)),
            "Player8": Data("Player8", CreateLeaderBoardDictionary(0x024BA4FC, 0x024BA580, 0x024BA8A4, 0x024BA74C, 0x024BA794, 0x024BA770, 0x024BA7B8, 0x024BA838, 0x024BA728, 0x024BA594, 0x120BA4C))
        }

    def PlayerDataString(self):
        s = ""
        for player, data in self.playerdata.items():
            sdata = str(data)
            if sdata == "":
                continue
            s += sdata + ",\n"

        s = s[:-2]
        s += "\n}"
        return s

    def LeaderboardString(self):
        active = False
        for key, value in self.leaderboard.items():
            if value.dataset["Housing"]["Value"] != 0:
                active = True

        if not active:
            return {}

        return json.dumps(leaderboard, indent=4)

PROCESS_WM_READ = 0x0010

from time import sleep
from pymem import Pymem

import psutil
import traceback

def GetProcessesByName(name):
    return [process for process in psutil.process_iter() if process.name() == name]

class Reader:
    def run(self):
        memorymap = MemoryMap()
        print("Searching for process...")
        pm = Pymem("Stronghold_Crusader_Extreme.exe")
        #print(dir(pm))
        print("Attached.")
        while True:
            try:
                self.UpdateGameData(pm, memorymap.playerdata)
                self.UpdateGameData(pm, memorymap.leaderboard)

                print(memorymap.PlayerDataString())
                print(memorymap.LeaderboardString())

                sleep(1)
            except IndexError as e:
                print(e)
                sleep(0.1)

            except Exception as e:
                print(e)
                traceback.print_exc()

    def UpdateGameData(self, pm, gameData):
        for name, data in gameData.items():
            for key, vdict in data.dataset.items():
                addr = vdict["Address"]
                size = vdict["Size"]
                if key == "Name":
                    value = pm.read_string(addr)
                else:
                    value = pm.read_int(addr)

                vdict["value"] = value

if __name__ == "__main__":
    reader = Reader()
    reader.run()
