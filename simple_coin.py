from blockchain import Blockchain

#Initiates blockchain

def generate_blocks(number_of_blocks):
    """
    input: number_of_blocks: int
    output: block Object

    Given a number of blocks return the output after x amount of block as a string. Input blocks are EMPTY
    """
    simple_chain = [Blockchain.genesis()]
    parent_block = simple_chain[0]

    for i in range(number_of_blocks):
        child_block = Blockchain.mine(parent_block)
        simple_chain.append(child_block)
        parent_block = child_block


    return child_block.hash
