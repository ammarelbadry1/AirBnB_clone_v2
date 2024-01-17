#!/usr/bin/python3
""" module to test Amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ testing class for Amenity class"""

    def __init__(self, *args, **kwargs):
        """ constructor method"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ method tests Amenity class """
        new = self.value()
        self.assertEqual(type(new.name), str)
