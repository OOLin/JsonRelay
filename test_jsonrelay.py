# test_jsonrelay.py
"""
Tests for JsonRelay module.
"""

import unittest
from jsonrelay import JsonRelay

class TestJsonRelay(unittest.TestCase):
    """Test cases for JsonRelay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JsonRelay()
        self.assertIsInstance(instance, JsonRelay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JsonRelay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
