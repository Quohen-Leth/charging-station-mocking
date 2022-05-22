import asyncio

import websockets

from src.settings import settings
from src.station.charge_point import ChargePointHandler


async def start_station(station_name):
    async with websockets.connect(
        f"ws://{settings.WEBSOCKETS_SERVER_HOST}:{settings.WEBSOCKETS_SERVER_PORT}/{station_name}",
        subprotocols=[settings.WEBSOCKETS_SUBPROTOCOL]
    ) as ws:
        charge_point = ChargePointHandler(station_name, ws)
        await asyncio.gather(
            charge_point.start(),
            charge_point.send_boot_notification(),
        )

