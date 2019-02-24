from json import dumps
import hashlib


# Our perfeunctionary hash function. We'll add to this later and make it more complex
# Takes an input block. Stringifies it and returns the sha256 of it using pythons default hashlib
def hash(block):
    return hashlib.sha256(dumps(block).encode('utf-8')).hexdigest()


# Basic proof of work. For any int n, find int m where hash(n * m) contains a set number of leading zeros
# Currently there's 4 zeroes needed. The difficulty increases exponentially with each 0 required.
# Let's try and get this to proof of stake in v2

def doWork(prevProof):

    proof = 0
    while verifyWork(prevProof, proof) == False:
        proof = proof + 1
    return proof

def verifyWork(prevProof, proof):
    return hashlib.sha256(str(prevProof).encode('utf-8') + str(proof).encode('utf-8')).hexdigest()[:5] == '00000'


