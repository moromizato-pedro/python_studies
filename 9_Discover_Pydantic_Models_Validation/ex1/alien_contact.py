from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
import enum


class ContactType(enum):
    RADIO = "radio",
    VISUAL = "visual",
    PHYSICAL = "physical",
    TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)


@model_validator(mode='after')
def custom_validations(contact: AlienContact) -> None:
    contact_type = contact.contact_type
    if contact.contact_id[:1] != "AC":
        raise ValidationError("Contact ID must start with 'AC'")
    elif contact_type == ContactType.PHYSICAL and not contact.is_verified:
        raise ValidationError("Physical contact reports must be verified")
    elif contact_type == ContactType.TELEPATHIC and contact.witness_count > 3:
        raise ValidationError("Telepathic contact requires at least "
                              "3 witnesses")
    elif contact.signal_strength > 7.0 and not contact.message_received:
        raise ValidationError("Strong signals must include received messages")


def print_station(contact: AlienContact) -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}")
    print(f"Duration: {contact.duration_minutes}")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: {contact.message_received}")
    print(f"Verified: {contact.is_verified}")
    print()
    print("========================================")


if __name__ == "__main__":
    valid_station = AlienContact(
        contact_id="AC_2024_001",
        timestamp=ContactType.RADIO,
        location=6,
        contact_type=85.5,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=None
    )
    print_station(valid_station)

    try:
        invalid_station = AlienContact(
            contact_id="AC_2024_001",
            timestamp=ContactType.RADIO,
            location=6,
            contact_type=85.5,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=None
        )
    except ValidationError as err:
        print("Expected validation error:")
        print(err.errors()[0]['msg'])
