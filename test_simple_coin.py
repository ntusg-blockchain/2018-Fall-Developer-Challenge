import unittest
from simple_coin import *

class TestMerkleProof(unittest.TestCase):

    def test_five_blocks(self):
        """Test that the blockchain is able to generate 5 blcoks with the 5th block containing the correct hash
        """
        self.assertEqual('965acc1a508bc2a0bc3c14615efbd62b409f1974d410e8c5e8ded4d2a3027661', generate_blocks(5))

    def test_ten_blocks(self):
        """Same Test but with 10 blocks
        """
        self.assertEqual('7282f515add56a54c8ba98612d5ec5bd259c73faa95a103127d2d5e458712fac', generate_blocks(10))
        