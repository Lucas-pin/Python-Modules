from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
from pydantic import PastDatetime, ValidationError
import json

SPACE_STATIONS = [
    {
        'station_id': 'LGW125',
        'name': 'Titan Mining Outpost',
        'crew_size': 6,
        'power_level': 76.4,
        'oxygen_level': 95.5,
        'last_maintenance': '2023-07-11T00:00:00',
        'is_operational': True,
        'notes': None
    },
    {
        'station_id': 'QCH189',
        'name': 'Deep Space Observatory',
        'crew_size': 3,
        'power_level': 70.8,
        'oxygen_level': 88.1,
        'last_maintenance': '2023-08-24T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    },
    {
        'station_id': 'ISS674',
        'name': 'Europa Research Station',
        'crew_size': 11,
        'power_level': 82.0,
        'oxygen_level': 91.4,
        'last_maintenance': '2023-10-21T00:00:00',
        'is_operational': True,
        'notes': None
    },
    {
        'station_id': 'ISS877',
        'name': 'Mars Orbital Platform',
        'crew_size': 9,
        'power_level': 79.7,
        'oxygen_level': 87.2,
        'last_maintenance': '2023-10-06T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    },
    {
        'station_id': 'LGW194',
        'name': 'Deep Space Observatory',
        'crew_size': 4,
        'power_level': 80.2,
        'oxygen_level': 89.9,
        'last_maintenance': '2023-10-25T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    },
    {
        'station_id': 'ISS847',
        'name': 'Solar Wind Monitor',
        'crew_size': 11,
        'power_level': 73.6,
        'oxygen_level': 98.1,
        'last_maintenance': '2023-12-11T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    },
    {
        'station_id': 'QCH400',
        'name': 'Asteroid Belt Relay',
        'crew_size': 12,
        'power_level': 75.5,
        'oxygen_level': 86.0,
        'last_maintenance': '2023-07-15T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    },
    {
        'station_id': 'ERS891',
        'name': 'Titan Mining Outpost',
        'crew_size': 4,
        'power_level': 94.4,
        'oxygen_level': 97.3,
        'last_maintenance': '2023-09-25T00:00:00',
        'is_operational': True,
        'notes': 'All systems nominal'
    },
    {
        'station_id': 'ABR266',
        'name': 'Asteroid Belt Relay',
        'crew_size': 8,
        'power_level': 76.0,
        'oxygen_level': 88.8,
        'last_maintenance': '2023-07-10T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    },
    {
        'station_id': 'LGW723',
        'name': 'Mars Orbital Platform',
        'crew_size': 11,
        'power_level': 90.8,
        'oxygen_level': 87.3,
        'last_maintenance': '2023-09-25T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    }
]


INVALID_SPACE_STATIONS = [
  {
    "station_id": "TOOLONG123456",
    "name": "Test Station",
    "crew_size": 25,
    "power_level": 85.0,
    "oxygen_level": 92.0,
    "last_maintenance": "2024-01-15T10:30:00",
    "is_operational": True
  },
  {
    "station_id": "TS",
    "name": "",
    "crew_size": 0,
    "power_level": -10.0,
    "oxygen_level": 150.0,
    "last_maintenance": "2024-01-15T10:30:00",
    "is_operational": True
  }
]


class SpaceStation(BaseModel):
    # Force Pydantic to validate assignment to fields after object creation
    model_config = ConfigDict(validate_assignment=True)

    station_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=1, max_length=50)]
    crew_size: Annotated[int, Field(ge=1, le=20)]
    power_level: Annotated[float, Field(ge=0.0, le=100.0)]
    oxygen_level: Annotated[float, Field(ge=0.0, le=100.0)]
    last_maintenance: PastDatetime
    is_operational: bool = Field(default=True)
    notes: Annotated[str | None, Field(max_length=200)] = None

    def display_info(self) -> None:
        print(f"Valid station created: {self.station_id}")
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size}")
        print(f"Power: {self.power_level:.2f}")
        print(f"Oxygen: {self.oxygen_level:.2f}")
        print("Last Maintenance: "
              f"{self.last_maintenance.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Status: "
              f"{'Operational' if self.is_operational else 'Inoperative'}")
        if self.notes is not None:
            print(f"Notes: {self.notes}")


def create_space_stations(raw_data: list[dict[str, str]]) -> None:
    for index, item in enumerate(raw_data):
        try:
            station = SpaceStation.model_validate(item)
            station.display_info()
            print("-"*50)
        except ValidationError as ex:
            for error in ex.errors():
                field = error["loc"][1] \
                        if len(error["loc"]) > 1 else "Object error"
                print(f"[Error] Object index {index} - "
                      f"Invalid field: '{field}' : {error['msg']}")


def main() -> None:
    print("Space Station Data Validation")
    print("="*50)
    try:
        json_string = json.dumps(SPACE_STATIONS)
        raw_data: list[dict[str, str]] = json.loads(json_string)
        create_space_stations(raw_data)

        print("="*50)
        json_string = json.dumps(INVALID_SPACE_STATIONS)
        raw_data = json.loads(json_string)
        create_space_stations(raw_data)
    except Exception as e:
        print(f"[Error] Unexpected error: {e}")


if __name__ == "__main__":
    main()
