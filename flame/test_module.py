import unittest
from flame import flame_names, merge_names

# run test from CLI with python3 -m unittest -v test_module.py

class TestRelationship(unittest.TestCase):
  def test_names(self):
        name1 = "steven"
        name2 = "christine"
        self.assertEqual(merge_names(name1, name2), "vechrii")

  def test_flame(self):
        merged_name = "vechrii"
        self.assertEqual(flame_names(merged_name), "married")