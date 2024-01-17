#!/usr/bin/python3
""" unittest module for User class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ test class for User class"""

    def __init__(self, *args, **kwargs):
        """ constructor method"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ method tests User class"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ method tests User class"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ method tests User class """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ method tests User class"""
        new = self.value()
        self.assertEqual(type(new.password), str)
