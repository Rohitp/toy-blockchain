from flask import Flask, jsonify, request
from blockchain import Blockchain
import sys
from utils import doWork, hash

# TODO: Add a unique node identifier
# TODO: Add a block reward, consensus algorithm and persistence

app = Flask(__name__)


blockchain = Blockchain()

@app.route('/transactions', methods=['GET'])
def getTransactions():
    return jsonify(blockchain.latestBlock['transactions']), 200

@app.route('/transactions', methods=['POST'])
def createTransaction():
    transactionData = request.get_json()
    required = ['sender', 'receiver', 'amount']
    params = list(transactionData.keys())
    missingParams = list(set(required) - set(params))
    if len(missingParams) > 0:
        print(list(set(required) - set(params)), file=sys.stderr)
        return jsonify("Parameters "+",".join(missingParams)+" are missing and required"), 400

    blockID = blockchain.createTransaction(transactionData['sender'], transactionData['receiver'], transactionData['amount'])
    return jsonify("Transaction Created In Block "+str(blockID)), 201



@app.route('/chain', methods=['GET'])
def getChain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/chain', methods=['POST'])
def mine():
    lastProof = blockchain.latestBlock['pow']
    proof = doWork(lastProof)
    block = blockchain.createBlock(pow=proof)
    return jsonify(block), 201







if __name__ == '__main__':
   app.run(debug=True)