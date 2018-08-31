from block import Block
import datetime as date

#creates genesis block
class Blockchain:
    def __init__(self):
        self.genesis()

    #Your address is 0xd3adb33f and you will be sending to yourself 100 coins as a reward for coming up with this wonderful framework
    def genesis():
        return Block(transaction='0xd3adb33f', value = 100)

    def mine(parent_block, transactions=None, value=0):
        child_height = parent_block.height + 1
        child_timestamp = '31 Aug 2018 11:00:00'
        # child_timestamp = date.datetime.now()
        parent_hash = parent_block.hash
        return Block(transactions, value, parent_hash, child_height, child_timestamp)