# test_drafttie.py
"""
Tests for DraftTie module.
"""

import unittest
from drafttie import DraftTie

class TestDraftTie(unittest.TestCase):
    """Test cases for DraftTie class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftTie()
        self.assertIsInstance(instance, DraftTie)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftTie()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
