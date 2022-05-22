from collections import defaultdict
import weakref


class StationCounterMixin:
    """ Mixin class to get running Charging Stations.
    Started Charging Stations stored as weak references
    to instances of ChargePointHandler class.
    """
    __refs__ = defaultdict(list)

    def __init__(self, *args, **kwargs):
        super(StationCounterMixin, self).__init__(*args, **kwargs)
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_stations(cls):
        """ Get all running stations."""
        stations = []
        for reference in cls.__refs__[cls]:
            station = reference()
            if station is not None:
                stations.append(station)
        return stations

    @classmethod
    def get_station(cls, station_id: str):
        """ Get running station with exact station_id."""
        for reference in cls.__refs__[cls]:
            station = reference()
            if station is not None and station.id == station_id:
                return station
