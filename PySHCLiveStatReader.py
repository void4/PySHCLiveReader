import json



class Meta:
    def __init__(self, name, addr, size=4, typ="i"):
        self.name = name
        self.addr = addr
        self.size = size
        self.typ = typ
        self.value = None

    def __repr__(self):
        return f"{self.name}: {self.value}"

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

PROCESS_WM_READ = 0x0010

from time import sleep
from pymem import Pymem

import psutil
import traceback

def GetProcessesByName(name):
    return [process for process in psutil.process_iter() if process.name() == name]

class Reader:

    def __init__(self, config):
        self.data = []

        config = config.splitlines()

        headerdata = config[0].split()
        header = []

        for column in headerdata:
            splitcolumn = column.split(":")
            name = splitcolumn[0]
            size = splitcolumn[1]
            if len(splitcolumn) >= 3:
                typ = splitcolumn[2]
            else:
                typ = "i"
            meta = [name, int(size), typ]
            header.append(meta)

        for row in config[1:]:
            self.data.append([])
            for column, value in enumerate(row.split()):
                try:
                    addr = int(value, 16)
                except ValueError:
                    addr = None
                self.data[-1].append(Meta(header[column][0], addr, header[column][1], header[column][2]))

    def run(self):
        print("Searching for process...")
        self.pm = Pymem("Stronghold_Crusader_Extreme.exe")
        #print(dir(pm))
        print("Attached.")
        while True:
            try:
                self.update()

                print(self.data)
                #print(memorymap.LeaderboardString())

                sleep(1)
            except IndexError as e:
                print(e)
                sleep(0.1)

            except Exception as e:
                print(e)
                traceback.print_exc()

    def update(self):
        for row in self.data:
            for column in row:
                if column.addr is None:
                    continue
                if column.typ == "i":
                    value = self.pm.read_int(column.addr)
                elif column.typ == "s":
                    value = self.pm.read_string(column.addr)
                else:
                    raise ValueError("Unknown column type:", column.typ)
                column.value = value

#V1.2.1-E
V1_2_1_E = """Name:32 Gold:4 Units:4 Popularity:4 Population:2 Housing:2
- 0x122c760
- 0x1230154
- 0x1233b48
- 0x123753c
- 0x123af30
- 0x123e924
- 0x1242318
- 0x1245d0c"""

V1_UNKNOWN = """Name:32:s Gold:4 Units:4 Popularity:4 Population:2 Housing:2
0x024BA286 0x011F2938 0x011F27E4 0x011F2870 0x011F45AC 0x011F24A0
0x024BA2E0 0x011F632C 0x011F61D8 0x011F6264 0x011F7FA0 0x011F5E94
0x024BA33A 0x011F9D20 0x011F9BCC 0x011F9C58 0x011FB994 0x011F9888
0x024BA394 0x011FD714 0x011FD5C0 0x011FD64C 0x011FF388 0x011FD27C
0x024BA3EE 0x01201108 0x01200fb4 0x01201040 0x01202D7C 0x01200C70
0x024BA448 0x01204AFC 0x012049A8 0x01204A34 0x01206770 0x01204664
0x024BA4A2 0x012084F0 0x0120839C 0x01208428 0x0120A164 0x01208058
0x024BA4FC 0x0120BEE4 0x0120BD90 0x0120BE1C 0x0120DB58 0x120BA4C
"""

if __name__ == "__main__":
    reader = Reader(V1_2_1_E)
    reader.run()
