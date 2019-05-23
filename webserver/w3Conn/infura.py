from web3 import Web3

with open('abi') as f:
    contract_abi = f.read()
contract = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/6de59f77f06e447a89d8fecdcbc9017d")).eth.contract(address = "0xd3a1e343f537aa7cf26042c3b09852c139a0d1d4", abi = contract_abi)