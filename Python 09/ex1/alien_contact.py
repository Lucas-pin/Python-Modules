from enum import Enum
from pydantic import BaseModel, Field, ValidationError, PastDatetime
from pydantic import model_validator
from typing import Annotated
import json

ALIEN_CONTACTS = [
    {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'visual',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 11,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_002',
        'timestamp': '2024-08-20T00:00:00',
        'location': 'Mauna Kea Observatory, Hawaii',
        'contact_type': 'radio',
        'signal_strength': 5.6,
        'duration_minutes': 152,
        'witness_count': 6,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_003',
        'timestamp': '2024-11-15T00:00:00',
        'location': 'Very Large Array, New Mexico',
        'contact_type': 'telepathic',
        'signal_strength': 4.5,
        'duration_minutes': 19,
        'witness_count': 14,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_004',
        'timestamp': '2024-02-24T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'telepathic',
        'signal_strength': 2.4,
        'duration_minutes': 46,
        'witness_count': 9,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_005',
        'timestamp': '2024-09-10T00:00:00',
        'location': 'SETI Institute, California',
        'contact_type': 'telepathic',
        'signal_strength': 6.4,
        'duration_minutes': 134,
        'witness_count': 5,
        'message_received': 'Warning about solar flare activity',
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_006',
        'timestamp': '2024-02-02T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'radio',
        'signal_strength': 2.7,
        'duration_minutes': 20,
        'witness_count': 14,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_007',
        'timestamp': '2024-03-25T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'physical',
        'signal_strength': 9.0,
        'duration_minutes': 138,
        'witness_count': 10,
        'message_received': 'Request for peaceful contact',
        'is_verified': True
    },
    {
        'contact_id': 'AC_2024_008',
        'timestamp': '2024-11-30T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'radio',
        'signal_strength': 8.6,
        'duration_minutes': 122,
        'witness_count': 13,
        'message_received': 'Unknown language pattern identified',
        'is_verified': True
    },
    {
        'contact_id': 'AC_2024_009',
        'timestamp': '2024-09-27T00:00:00',
        'location': 'Mauna Kea Observatory, Hawaii',
        'contact_type': 'visual',
        'signal_strength': 2.1,
        'duration_minutes': 25,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_010',
        'timestamp': '2024-06-12T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'physical',
        'signal_strength': 4.3,
        'duration_minutes': 52,
        'witness_count': 11,
        'message_received': None,
        'is_verified': True
    },
    {
        'contact_id': 'AC_2024_011',
        'timestamp': '2024-11-05T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'radio',
        'signal_strength': 3.7,
        'duration_minutes': 235,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_012',
        'timestamp': '2024-07-04T00:00:00',
        'location': 'International Space Station',
        'contact_type': 'radio',
        'signal_strength': 5.3,
        'duration_minutes': 111,
        'witness_count': 10,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_013',
        'timestamp': '2024-02-12T00:00:00',
        'location': 'Antarctic Research Station',
        'contact_type': 'visual',
        'signal_strength': 6.8,
        'duration_minutes': 228,
        'witness_count': 11,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_014',
        'timestamp': '2024-10-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'radio',
        'signal_strength': 7.2,
        'duration_minutes': 113,
        'witness_count': 8,
        'message_received': 'Mathematical sequence detected: prime numbers',
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_015',
        'timestamp': '2024-01-02T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'radio',
        'signal_strength': 2.1,
        'duration_minutes': 9,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    }
]

INVALID_ALIEN_CONTACTS = [
  {
    "contact_id": "WRONG_FORMAT",
    "timestamp": "2024-01-15T14:30:00",
    "location": "Area 51",
    "contact_type": "radio",
    "signal_strength": 8.5,
    "duration_minutes": 45,
    "witness_count": 5,
    "message_received": None,
    "is_verified": False
  },
  {
    "contact_id": "AC_2024_002",
    "timestamp": "2024-01-16T09:15:00",
    "location": "Roswell",
    "contact_type": "telepathic",
    "signal_strength": 6.2,
    "duration_minutes": 30,
    "witness_count": 1,
    "message_received": None,
    "is_verified": False
  }
]


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: Annotated[str, Field(min_length=5, max_length=15)]
    timestamp: PastDatetime
    location: Annotated[str, Field(min_length=3, max_length=100)]
    contact_type: ContactType
    signal_strength: Annotated[float, Field(ge=0.0, le=10.0)]
    duration_minutes: Annotated[int, Field(ge=1, le=1440)]
    witness_count: Annotated[int, Field(ge=1, le=100)]
    message_received: Annotated[str | None, Field(max_length=500)]
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_id(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        return self

    @model_validator(mode="after")
    def validate_physical_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def validate_telephatic_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.TELEPATHIC and \
           self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least "
                             "3 witnesses")
        return self

    @model_validator(mode="after")
    def validate_strong_signal(self) -> "AlienContact":
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should "
                             "include received messages")
        return self

    def display_contact_info(self) -> None:
        for k, v in self.__dict__.items():
            comment: str = ""
            formatted_property = k.replace("_", " ").title()

            match formatted_property:
                case _ if "Signal" in formatted_property:
                    comment = "/10"
                case _ if "Duration" in formatted_property:
                    comment = " minutes"
                case _ if "Message" in formatted_property:
                    v = f"'{v}'"

            print(f"{formatted_property}: {v}{comment}")


def create_alien_contact(raw_data: list[dict[str, str]]) -> None:
    for index, item in enumerate(raw_data):
        try:
            contact = AlienContact.model_validate(item)
            contact.display_contact_info()
            print("-"*50)
        except ValidationError as ex:
            for error in ex.errors():
                field = error["loc"][-1] \
                        if error["loc"] else "Object error"
                print(f"[Error] Object index: {index} - "
                      f"Invalid field: '{field}' : {error['msg']}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("="*50)
    try:
        json_string = json.dumps(ALIEN_CONTACTS)
        raw_data: list[dict[str, str]] = json.loads(json_string)
        create_alien_contact(raw_data)
        print("="*50)
        json_string = json.dumps(INVALID_ALIEN_CONTACTS)
        raw_data = json.loads(json_string)
        create_alien_contact(raw_data)
    except Exception as e:
        print(f"[Error] Unexpected error: {e}")


if __name__ == "__main__":
    main()
