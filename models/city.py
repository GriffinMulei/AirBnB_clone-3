#!/usr/bin/python3
"""Defines the city class."""
from models.base_models import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
    state_id (str): The state id.
    name (str): The name of the city.
    """

    state_id = ""
    name = ""
