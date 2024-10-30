from pydantic import BaseModel


class AwsConfig(BaseModel):
    region: str | None = None
    endpoint: str | None = None
