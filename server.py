from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    return jsonify("Hello, World"), 200


blockchain = Blockchain()



@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
   app.run(debug=True)