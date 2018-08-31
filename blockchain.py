from block import Block
import datetime as date

#creates genesis block
class Blockchain:
    def __init__(self):
        self.genesis()
        
    def genesis():
        return Block()

    def mine(parent_block, transactions=None):
        child_height = parent_block.height + 1
        child_timestamp = '31 Aug 2018 11:00:00'
        # child_timestamp = date.datetime.now()
        parent_hash = parent_block.hash
        return Block(transactions, parent_hash, child_height, child_timestamp)