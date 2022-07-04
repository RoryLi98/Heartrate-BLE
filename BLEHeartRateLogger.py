from ast import While
import asyncio
import os
import time 
import sys
from bleak import BleakScanner

async def SeachBLEDevices():
    devicesInfo = await BleakScanner.discover()
    print("\r", end="")
    for deviceInfo in devicesInfo:
        print(deviceInfo.name)
    os.system("pause")
    sys.exit() 

async def Waiting():
    intiTime = int(time.time()%4)
    while(True):
        dotCount = (int(time.time()%4) - intiTime + 4)%4
        print(F"\rSearching{'.' * dotCount}{' '*(3-dotCount)}", end="")
        await asyncio.sleep(0.1)


async def main():
    waitTask = asyncio.create_task(Waiting()) # 创建task任务
    searchTask = asyncio.create_task(SeachBLEDevices()) # 创建task任务
    tasks = [searchTask, waitTask]
    await asyncio.wait(tasks)

asyncio.run(main())
