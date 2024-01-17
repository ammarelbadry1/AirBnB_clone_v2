#!/usr/bin/python3
""" unitest module for Review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ test class for Review class"""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ method tests Review class"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ method tests Review class """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ method tests Review class """
        new = self.value()
        self.assertEqual(type(new.text), str)
