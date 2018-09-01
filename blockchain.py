from block import Block
import datetime as date

#creates genesis block
class Blockchain:
    blocks = []
    def __init__(self):
        self.genesis()

    def __str__(self):
        return str(self.blocks)

    #Your address is 0xd3adb33f and you will be sending to yourself 100 coins as a reward for coming up with this wonderful framework
    def genesis(self):
        self.blocks.append(Block(transaction='0xd3adb33f', value = 100)) 

    def get_current_block(self):
        return self.blocks[len(self.blocks)-1]

    def mine(self, parent_block, transactions=None, value=0):
        child_height = parent_block.height + 1
        parent_hash = parent_block.hash
        self.blocks.append(Block(transactions, value, parent_hash, child_height))

    __repr__ = __str__