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

PROCESS_WM_READ = 0x0010

from time import sleep
from pymem import Pymem

import psutil
import traceback

def GetProcessesByName(name):
    return [process for process in psutil.process_iter() if process.name() == name]

class MemoryReader:

    def __init__(self, exename, tables):
        self.exename = exename
        self.tables = tables
        for name, table in self.tables.items():
            self.tables[name] = self.loadTable(table)

        self.attach()

    def loadTable(self, table):
        config = table.splitlines()

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

        data = []

        for row in config[1:]:
            data.append([])
            for column, value in enumerate(row.split()):
                try:
                    addr = int(value, 16)
                except ValueError:
                    addr = None
                data[-1].append(Meta(header[column][0], addr, header[column][1], header[column][2]))

        return data

    def attach(self):
        print("Searching for process...")
        self.pm = Pymem(self.exename)
        #print(dir(pm))
        print("Attached.")

    def run(self):

        while True:
            try:
                self.update()

                print(self.tables)

                sleep(1)
            except IndexError as e:
                print(e)
                sleep(0.1)

            except Exception as e:
                print(e)
                traceback.print_exc()

    def runOnce(self):
        self.update()
        return self.tables

    def update(self):
        for name, table in self.tables.items():
            for row in table:
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
