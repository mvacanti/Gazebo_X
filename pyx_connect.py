
import asyncio
from mavsdk import System
import xpc

async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Start the tasks
    asyncio.ensure_future(print_position(drone))
    asyncio.ensure_future(print_euler(drone))



async def print_position(drone):
    async for position in drone.telemetry.position():
        client.sendPOSI([position.latitude_deg, position.longitude_deg, position.absolute_altitude_m, -998,
                         -998, -998, 0])

async def print_euler(drone):
    async for rpy in drone.telemetry.attitude_euler():
        client.sendPOSI([-998, -998, -998, rpy.pitch_deg, rpy.roll_deg, rpy.yaw_deg, 0])


client = xpc.XPlaneConnect("192.168.2.24", 49009, 0, 1000)


if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()