from enum import Enum
from pydantic import BaseModel, Field, ValidationError, PastDatetime
from pydantic import model_validator, field_validator
from typing import Annotated
import json


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

    @field_validator("contact_id")
    @classmethod
    def validate_id(cls, value: str) -> str:
        if not value.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        return value

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


def main() -> None:
    print("Alien Contact Log Validation")
    print("="*50)
    with open("../generated_data/invalid_contacts.json", "r") as f:
        raw_data: list[dict[str, str]] = json.loads(f.read())
        valid_contacts: list[AlienContact] = []
        for index, item in enumerate(raw_data):
            try:
                contact = AlienContact.model_validate(item)
                valid_contacts.append(contact)
                contact.display_contact_info()
                print("-"*50)
            except ValidationError as ex:
                for error in ex.errors():
                    field = error["loc"][-1] \
                            if error["loc"] else "Object error"
                    print(f"[Error] Object index: {index} - "
                          f"Invalid field: '{field}' : {error['msg']}")


if __name__ == "__main__":
    main()
