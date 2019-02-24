from time import time
from utils import hash

class Blockchain(object):
    def __init__(self):
        self.transactions  = []
        self.chain = []

        # The genesis block. Seeding it manually. 
        self.createBlock(5, -1)


    # These comments don't follow the python docsring format, but fuck it,
    # I'm too lazy. This adds a simple transaction dict to a list and returns the block that contains the transaction
    # sender - randomly generated address - string
    # receiver - randomly generated address - string
    # amount - float 
    def createTransaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
        })

        return self.chain[-1]['id'] + 1

    def createBlock(self, pow, prevHash = None):
        block = {
            'id': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'pow': pow,
            'prevHash': prevHash or hash(self.chain[-1])
        }

         # We've created transactions for this block. Clear them so we can start making a new list of transactions for the next block
        self.transactions = []
        self.chain.append(block)

        return block

    @property
    def latestBlock(self):
        return self.chain[-1]

  


blockchain = Blockchain()

# Seeding the genesis block manually.
# blockchain.chain.append({ 'id': 1, 'timestamp': time(), 'proof': 5, 'prevHash': -1})

