from web3 import Web3

with open('w3Conn/abi') as f:
    contract_abi = f.read()
web3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/6de59f77f06e447a89d8fecdcbc9017d"))
contract = web3.eth.contract(address = "0xfd220453e84762842bae8f1ed64e50dcf2141d7d", abi = contract_abi)