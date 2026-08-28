# test_crestforge.py
"""
Tests for CrestForge module.
"""

import unittest
from crestforge import CrestForge

class TestCrestForge(unittest.TestCase):
    """Test cases for CrestForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestForge()
        self.assertIsInstance(instance, CrestForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
