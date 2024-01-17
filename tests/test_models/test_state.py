#!/usr/bin/python3
""" unittest module for State class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ test class for State class"""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """  method tests Review class """
        new = self.value()
        self.assertEqual(type(new.name), str)
