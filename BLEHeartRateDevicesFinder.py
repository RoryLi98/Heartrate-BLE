import asyncio
import os
import time
from bleak import BleakScanner

async def Waiting():
    while(True):
        initStr = "."
        initStr += "." for _ in range(int(time.time()%3))
        print(f"\rSearching{initStr}}") 

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(type(d))
        # print(f"\r{for _ in range(int(time.time()%3))}}") 
print("Searching...")
asyncio.run(main())
os.system("pause")