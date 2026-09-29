from enum import Enum
import json
from pydantic import BaseModel, Field, ValidationError
from pydantic import model_validator
from typing import Annotated
from datetime import datetime

SPACE_MISSIONS = [
    {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    },
    {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Jupiter Orbit Colony Mission',
        'destination': 'Jupiter Orbit',
        'launch_date': '2024-10-01T00:00:00',
        'duration_days': 1065,
        'crew': [
            {
                'member_id': 'CM011',
                'name': 'Emma Brown',
                'rank': 'commander',
                'age': 49,
                'specialization': 'Mission Command',
                'years_experience': 27,
                'is_active': True
            },
            {
                'member_id': 'CM012',
                'name': 'John Hernandez',
                'rank': 'lieutenant',
                'age': 36,
                'specialization': 'Science Officer',
                'years_experience': 22,
                'is_active': True
            },
            {
                'member_id': 'CM013',
                'name': 'Sofia Rodriguez',
                'rank': 'commander',
                'age': 29,
                'specialization': 'Life Support',
                'years_experience': 20,
                'is_active': True
            },
            {
                'member_id': 'CM014',
                'name': 'Sofia Lopez',
                'rank': 'lieutenant',
                'age': 44,
                'specialization': 'Systems Analysis',
                'years_experience': 25,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4626.0
    },
    {
        'mission_id': 'M2024_EUROPA',
        'mission_name': 'Europa Colony Mission',
        'destination': 'Europa',
        'launch_date': '2024-02-07T00:00:00',
        'duration_days': 666,
        'crew': [
            {
                'member_id': 'CM021',
                'name': 'Lisa Garcia',
                'rank': 'captain',
                'age': 36,
                'specialization': 'Medical Officer',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'CM022',
                'name': 'John Garcia',
                'rank': 'cadet',
                'age': 46,
                'specialization': 'Security',
                'years_experience': 25,
                'is_active': True
            },
            {
                'member_id': 'CM023',
                'name': 'Michael Johnson',
                'rank': 'officer',
                'age': 54,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM024',
                'name': 'Sarah Rodriguez',
                'rank': 'lieutenant',
                'age': 54,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM025',
                'name': 'Maria Smith',
                'rank': 'cadet',
                'age': 38,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4976.0
    },
    {
        'mission_id': 'M2024_LUNA',
        'mission_name': 'Mars Colony Mission',
        'destination': 'Mars',
        'launch_date': '2024-06-13T00:00:00',
        'duration_days': 222,
        'crew': [
            {
                'member_id': 'CM031',
                'name': 'Anna Davis',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Communications',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM032',
                'name': 'Elena Garcia',
                'rank': 'lieutenant',
                'age': 42,
                'specialization': 'Science Officer',
                'years_experience': 23,
                'is_active': True
            },
            {
                'member_id': 'CM033',
                'name': 'Anna Brown',
                'rank': 'officer',
                'age': 55,
                'specialization': 'Engineering',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM034',
                'name': 'Emma Smith',
                'rank': 'captain',
                'age': 37,
                'specialization': 'Research',
                'years_experience': 23,
                'is_active': True
            },
            {
                'member_id': 'CM035',
                'name': 'Sofia Smith',
                'rank': 'lieutenant',
                'age': 53,
                'specialization': 'Security',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM036',
                'name': 'Maria Hernandez',
                'rank': 'commander',
                'age': 41,
                'specialization': 'Medical Officer',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM037',
                'name': 'John Hernandez',
                'rank': 'officer',
                'age': 42,
                'specialization': 'Science Officer',
                'years_experience': 20,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4984.6
    },
    {
        'mission_id': 'M2024_EUROPA',
        'mission_name': 'Saturn Rings Research Mission',
        'destination': 'Saturn Rings',
        'launch_date': '2024-09-18T00:00:00',
        'duration_days': 602,
        'crew': [
            {
                'member_id': 'CM041',
                'name': 'William Davis',
                'rank': 'captain',
                'age': 35,
                'specialization': 'Medical Officer',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM042',
                'name': 'Sarah Smith',
                'rank': 'captain',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM043',
                'name': 'Elena Garcia',
                'rank': 'commander',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM044',
                'name': 'Sofia Williams',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Systems Analysis',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'CM045',
                'name': 'Sarah Jones',
                'rank': 'lieutenant',
                'age': 25,
                'specialization': 'Maintenance',
                'years_experience': 11,
                'is_active': True
            },
            {
                'member_id': 'CM046',
                'name': 'Lisa Rodriguez',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Life Support',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'CM047',
                'name': 'Sarah Smith',
                'rank': 'cadet',
                'age': 28,
                'specialization': 'Pilot',
                'years_experience': 8,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 1092.6
    }
]

INVALID_SPACE_MISSIONS = [
    {
        'mission_id': 'X123',
        'mission_name': 'Invalid Mission',
        'destination': 'Mars',
        'launch_date': '2025-01-01T00:00:00',
        'duration_days': 400,
        'crew': [],
        'mission_status': 'planned',
        'budget_millions': 500.0
    },
    {
        'mission_id': 'Y456',
        'mission_name': 'Another Invalid Mission',
        'destination': 'Jupiter',
        'launch_date': '2026-01-01T00:00:00',
        'duration_days': 500,
        'crew': [],
        'mission_status': 'planned',
        'budget_millions': 600.0
    }
]


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=2, max_length=50)]
    rank: Rank
    age: Annotated[int, Field(ge=18, le=80)]
    specialization: Annotated[str, Field(min_length=3, max_length=30)]
    years_experience: Annotated[int, Field(ge=0, le=50)]
    is_active: bool = True

    def display_member_info(self) -> None:
        properties = []

        for field_name, value in self:
            comment = ""
            formatted_property = field_name.replace("_", " ").title()

            if field_name in ("age", "years_experience"):
                comment = " years"

            properties.append(f"{formatted_property}: {value}{comment}")

        print(" - ".join(properties))


class SpaceMission(BaseModel):
    mission_id: Annotated[str, Field(min_length=5, max_length=15)]
    mission_name: Annotated[str, Field(min_length=3, max_length=100)]
    destination: Annotated[str, Field(min_length=3, max_length=50)]
    launch_date: datetime
    duration_days: Annotated[int, Field(ge=1, le=3650)]
    crew: Annotated[list[CrewMember], Field(min_length=1, max_length=12)]
    mission_status: str = "planned"
    budget_millions: Annotated[float, Field(ge=1.0, le=10000.0)]

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if self.mission_id.startswith("M"):
            return self
        raise ValueError("Mission ID must start with 'M'")

    @model_validator(mode="after")
    def validate_ranks(self) -> "SpaceMission":
        if any(member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER
               for member in self.crew):
            return self
        raise ValueError("Mission must have at least one Captain or Commander")

    @model_validator(mode="after")
    def validate_long_mission(self) -> "SpaceMission":
        if self.duration_days > 365:
            experienced_members: int = sum(1 for member in self.crew
                                           if member.years_experience > 5)
            if experienced_members >= len(self.crew) / 2:
                return self
            else:
                raise ValueError("Long missions (> 365 days) need 50\\% "
                                 "experienced crew (5+ years)")
        return self

    @model_validator(mode="after")
    def validate_all_active(self) -> "SpaceMission":
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def display_mission_info(self) -> None:
        for field_name, value in self:
            comment: str = ""
            formatted_property = field_name.replace("_", " ").title()

            if field_name == "duration_days":
                comment = " days"
            elif field_name == "budget_millions":
                comment = " M"
            elif field_name == "crew":
                num_members = len(value) if value is not None else 0
                comment = f"{num_members} members"
                value = ""
            print(f"{formatted_property}: {value}{comment}")

            if "Crew" in formatted_property:
                if field_name == "crew" and self.crew:
                    for member in self.crew:
                        if member is not None:
                            print("  ", end="")
                            member.display_member_info()


def create_space_mission(raw_data: list[dict[str, str]]) -> None:
    for index, mission in enumerate(raw_data):
        try:
            space_mission = SpaceMission.model_validate(mission)
            space_mission.display_mission_info()
            print("-"*50)
        except ValidationError as e:
            for error in e.errors():
                field = error["loc"][-1] if error["loc"] else "Object error"
                print(f"[Error] Object index: {index} - "
                      f"Invalid field: '{field}' : {error['msg']}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("="*50)
    try:
        json_string = json.dumps(SPACE_MISSIONS)
        data = json.loads(json_string)
        create_space_mission(data)
        print("="*50)
        json_string = json.dumps(INVALID_SPACE_MISSIONS)
        data = json.loads(json_string)
        create_space_mission(data)
    except Exception as e:
        print(f"[Error] Unexpected error: {e}")


if __name__ == "__main__":
    main()
