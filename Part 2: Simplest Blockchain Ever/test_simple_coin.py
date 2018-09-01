import unittest
from simple_coin import *

class TestMerkleProof(unittest.TestCase):

    def test_five_blocks(self):
        """Test that the blockchain is able to generate 5 blcoks with the 5th block containing the correct hash
        """
        self.assertEqual('9400b8b82ca50e77cb017aa910f5c7a31541b2c0a95a00fba41dec6da7e18da7', generate_blocks(5))

    def test_ten_blocks(self):
        """Same Test but with 10 blocks
        """
        self.assertEqual('ac328102ec4df7f81e5c6f9701ccd7d80d21c94fe716d40061562f1ebc967568', generate_blocks(10))
        