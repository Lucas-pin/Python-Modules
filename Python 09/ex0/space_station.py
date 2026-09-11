from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, PastDatetime

class SpaceStation(BaseModel):
    station_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=1, max_length=50)]
    crew_size: Annotated[int, Field(ge=1, le=20)]
    power_level: Annotated[float, Field(ge=0.0, le=100.0)]
    oxygen_level: Annotated[float, Field(ge=0.0, le=100.0)]
    last_maintenance: PastDatetime
    is_operational: bool = Field(default=True)
    notes = Annotated[str | None, Field(le=200)] = None