import asyncio
import os
import time 
import sys
import binascii
from bleak import BleakScanner
from _manufacturers import MANUFACTURERS

async def SeachBLEDevices():
    devicesInfo = await BleakScanner.discover()
    print("\r", end="")
    for deviceInfo in devicesInfo:
        if not deviceInfo.name:
            if "manufacturer_data" in deviceInfo.metadata:
                ks = list(deviceInfo.metadata["manufacturer_data"].keys())
                if len(ks):
                    mf = MANUFACTURERS.get(ks[0], MANUFACTURERS.get(0xFFFF))
                    valueX16Bytes = deviceInfo.metadata["manufacturer_data"].get(ks[0], MANUFACTURERS.get(0xFFFF))
                    valueBytes = binascii.hexlify(valueX16Bytes)
                    value = valueBytes.decode(encoding='unicode_escape')
                    print("{0} | {1} dBm | {2} ({3})".format(deviceInfo.address, deviceInfo.rssi, mf, value))
        else:
            print("{0} | {1} dBm | {2}".format(deviceInfo.address, deviceInfo.rssi, deviceInfo.name or "Unknown"))

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
    tasks = [searchTask]
    await asyncio.wait(tasks)

asyncio.run(main())
