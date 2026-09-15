from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
from pydantic import PastDatetime, ValidationError
from datetime import datetime


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
        print(f"Last Maintenance: \
              {self.last_maintenance.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Status: "
              f"{'Operational' if self.is_operational else 'Inoperative'}")
        if self.notes is not None:
            print(f"Notes: {self.notes}")


class main():
    print("Space Station Data Validation")
    print("="*50)
    try:
        station: SpaceStation = SpaceStation(
            station_id="ISS001", name="Internation Space Station",
            crew_size=6, power_level=85.5,
            oxygen_level=92.3, last_maintenance=datetime.now(),
            is_operational=True, notes="Amazing place to work!")

        station.display_info()
        print("="*50)
        invalid_station: SpaceStation = SpaceStation(
            station_id="ISS001", name="Invalid Station",
            crew_size=85, power_level=85.5,
            oxygen_level=105, last_maintenance=datetime.now(),
            is_operational=True)

        invalid_station.display_info()

    except ValidationError as ex:
        error_desc = [f"{str(error['loc'][0])}: {str(error['msg'])}"
                      for error in ex.errors()]
        for error in error_desc:
            print(error)


if __name__ == "__main__":
    main()
