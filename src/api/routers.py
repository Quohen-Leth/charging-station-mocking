import asyncio

from fastapi import APIRouter, HTTPException, status

from src.station.utils import start_station
from src.station.charge_point import ChargePointHandler


station_router = APIRouter()

station_tasks = {}


@station_router.get("/start")
async def start_charging_station(station_id: str):
    task = asyncio.create_task(start_station(station_id))
    station_tasks[station_id] = task
    return {"status": "ok"}


@station_router.get("/stop")
async def stop_charging_station(station_id: str):
    task = station_tasks.get(station_id, None)

    if task:
        task.cancel()
        # TODO: remove station instance
        station = ChargePointHandler.get_station(station_id)
        del station

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Charging Station {station_id} Not Found."
        )


@station_router.get("/stations")
async def view_started_charging_stations():
    return [station.id for station in ChargePointHandler.get_stations()]
