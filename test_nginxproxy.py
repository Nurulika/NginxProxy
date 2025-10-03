# test_nginxproxy.py
"""
Tests for NginxProxy module.
"""

import unittest
from nginxproxy import NginxProxy

class TestNginxProxy(unittest.TestCase):
    """Test cases for NginxProxy class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NginxProxy()
        self.assertIsInstance(instance, NginxProxy)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NginxProxy()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
