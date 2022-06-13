import sys
import platform
import logging
import asyncio
from bleak import BleakClient
from bleak import BleakClient
from bleak import _logger as logger
from bleak.uuids import uuid16_dict

HRT_RX_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

def notification_handler(sender, data):
    """
        notification handler which prints the data received.
    """
    print("current heartrate {0}".format(data[1]))

async def run(address, loop):

    async with BleakClient(address, loop=loop) as client:

        # wait for BLE client to be connected
        x = await client.is_connected()
        print("Now Connected: {0}".format(x))

        # wait for data to be sent from client
        await client.start_notify(HRT_RX_UUID, notification_handler)

        while True :

            #give some time to do other tasks
            await asyncio.sleep(0.01)

if __name__ == "__main__":

    # if provided take MAC address from command line
    if len(sys.argv) == 2:
        address = sys.argv[1]
    else:
        # this is MAC of the peripheral/server device hardcoded
        address = ("FC:16:DB:25:FC:41")

    # print("Heart rate client (version {})".format(__version__))
    # print("Looking for peripheral/server with address {}".format(address))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop))