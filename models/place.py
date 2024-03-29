#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        cty_id (str): the City id.
        usr_id (str): the User id.
        name (str): the name of the place.
        dscrption (str): the dscrption of the place.
        number_rooms (int): the number of rooms of the place.
        number_bathrooms (int): the number of bathrooms of the place.
        max_guest (int): the maximum number of guests of the place.
        price_by_night (int): the price by night of the place.
        latitude (float): the latitude of the place.
        longitude (float): the longitude of the place.
        amenity_ids (list): a list of Amenity ids.
    """

    cty_id = ""
    usr_id = ""
    name = ""
    dscrption = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
