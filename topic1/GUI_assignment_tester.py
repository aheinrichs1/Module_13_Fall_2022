"""
GUI_assignment_tester.py
Author: Alex Heinrichs
Date Created: 11/23/2022

Unit test for GUI assignment
"""
import unittest
from topic1.GUI_assignment import NumberGuesser


class GUITest(unittest.TestCase):
    def setUp(self):
        self.test_list = NumberGuesser()

    def tearDown(self):
        del self.test_list

    def test_constructor(self):
        self.assertEquals([], self.test_list.guessed_list)

    def test_adding_to_list(self):
        self.test_list.add_guess(2)
        self.test_list.add_guess(4)
        self.test_list.add_guess(6)
        self.assertEquals([2, 4, 6], self.test_list.guessed_list)
