from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physcial"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    contact_type: ContactType
    location: str = Field(min_length=3, max_length=100)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least 3 witnesses"
                             )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a received message")

        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-05-01T10:00:00",
            contact_type="radio",
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'\n")

    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    try:
        bad_contact = AlienContact(
            contact_id="AC_BAD",
            timestamp=datetime.now(),
            location="Unknown",
            contact_type="telepathic",
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
        )
        bad_contact = bad_contact
    except ValidationError as e:
        print("Expected validation error:")
        print("======================================")
        print(e)


if __name__ == "__main__":
    main()
