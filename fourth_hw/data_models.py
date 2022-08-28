from typing import List, Dict, Optional, Any

from pydantic import BaseModel, StrictStr, Field, StrictInt


class DogImages(BaseModel):
    message: List[StrictStr]
    status: StrictStr


class DogImage(BaseModel):
    message: StrictStr
    status: StrictStr


class AllBreeds(BaseModel):
    message: Dict[StrictStr, List[StrictStr]]
    status: StrictStr


class Brewer(BaseModel):
    brew_id: StrictStr = Field(alias='id')
    name: StrictStr
    brewery_type: StrictStr
    street: Optional[StrictStr]
    address_2: Optional[StrictStr]
    address_3: Optional[StrictStr]
    city: Optional[StrictStr]
    state: Optional[StrictStr]
    county_province: Optional[StrictStr]
    postal_code: Optional[StrictStr]
    country: Optional[StrictStr]
    longitude: Optional[StrictStr]
    latitude: Optional[StrictStr]
    phone: Optional[StrictStr]
    website_url: Optional[StrictStr]
    updated_at: Optional[StrictStr]
    created_at: Optional[StrictStr]


class CreateResourseModel(BaseModel):
    resourse_id: StrictInt=Field(alias='id')
    title: StrictStr
    body: Optional[StrictStr]
    userId: Optional[Any]
