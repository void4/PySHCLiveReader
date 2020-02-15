# PySHCLiveReader

Provides and optionally graphs live game statistics, ideal for tournaments!

![Live statistics](livestats.png)

## Installation
`pip install -r requirements.txt`

Note: --user

## Usage
Open a `cmd` with Administrator privileges

`python main.py`

## Manual config

If you are using a different Stronghold version, use `search.py` to search for the memory addresses, then update the config table.
There is one line for each player. The header row indicates the name of the cell, the size in bytes and the type (i=integer, s=string).
