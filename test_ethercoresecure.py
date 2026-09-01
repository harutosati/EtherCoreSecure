# test_ethercoresecure.py
"""
Tests for EtherCoreSecure module.
"""

import unittest
from ethercoresecure import EtherCoreSecure

class TestEtherCoreSecure(unittest.TestCase):
    """Test cases for EtherCoreSecure class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherCoreSecure()
        self.assertIsInstance(instance, EtherCoreSecure)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherCoreSecure()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
