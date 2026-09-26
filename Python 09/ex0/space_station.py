from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field
from pydantic import PastDatetime, ValidationError
import json


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


def main() -> None:
    print("Space Station Data Validation")
    print("="*50)

    with open("../generated_data/invalid_stations.json", "r") as f:
        raw_data: list[dict[str, str]] = json.loads(f.read())
        valid_contacts: list[SpaceStation] = []
        for index, item in enumerate(raw_data):
            try:
                station = SpaceStation.model_validate(item)
                valid_contacts.append(station)
                station.display_info()
                print("-"*50)
            except ValidationError as ex:
                for error in ex.errors():
                    field = error["loc"][1] \
                        if len(error["loc"]) > 1 else "Object error"
                    print(f"[Error] Object index {index} - "
                          f"Invalid field: '{field}' : {error['msg']}")


if __name__ == "__main__":
    main()
