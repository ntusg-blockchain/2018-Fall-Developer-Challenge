import unittest
from simple_coin import *

class TestMerkleProof(unittest.TestCase):

    def test_five_blocks(self):
        """Test that the blockchain is able to generate 5 blcoks with the 5th block containing the correct hash
        """
        self.assertEqual('5cab08c8154259290d863e90847c4bf6f7ed9133aaab387a2ddf90a34f8f1a22', generate_blocks(5))

    def test_ten_blocks(self):
        """Same Test but with 10 blocks
        """
        self.assertEqual('02e8649e4e5aa2214ca983067c29e8fe2b065515b8354a39ed25f6b493803091', generate_blocks(10))
        