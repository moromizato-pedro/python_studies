from pydantic import Field, model_validator, BaseModel


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=)
