from web3 import Web3
import json
import sys

contractAddress = "0xd4965421d40bed7d0de2b4ffa02fb118d3424195"
with open('abi.json', 'r') as f:
    contract_abi = json.load(f)
web3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/ws/v3/6de59f77f06e447a89d8fecdcbc9017d"))
contract = web3.eth.contract(address = Web3.toChecksumAddress(contractAddress), abi = contract_abi)
signData = bytes('지갑을 인증해 주세요.\nPlease verify your wallet.', encoding = 'utf-8')

def checkSign(signTypedData: str, address: str) -> bool:
    sign = contract.functions.checkSignature(
            signData,
            bytes.fromhex(signTypedData[2:66]),
            bytes.fromhex(signTypedData[66:130]),
            int(signTypedData[130:], 16)
        ).call()
    return sign == Web3.toChecksumAddress(address)

def getTradeState(trade_id):
    state = ['분양 중', '예약 중', '완료됨', '취소됨']
    return state[contract.functions.showTrade(trade_id).call()[2]]

# def watingTradeList(
# ageStart = 0: int,
# ageEnd = sys.maxint: int,
# gender = true: bool,
# breed = -1: int,
# size = -1: int,
# )