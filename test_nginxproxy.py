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
        # Create an instance of NginxProxy
        instance = NginxProxy()
        # Verify the instance is an instance of NginxProxy
        self.assertIsInstance(instance, NginxProxy)
        
    def test_run_method(self):
        """Test the run method."""
        # Create an instance of NginxProxy
        instance = NginxProxy()
        # Verify the run method returns True
        self.assertTrue(instance.run())

if __name__ == "__main__":
    # Run the test suite
    unittest.main()