import requests

API_KEY = "7E4MNJZMZA42DY2856XC3RR2DMYSVXKKHS"
ETHERSCAN_API = "https://api.etherscan.io/api"

def get_creation_tx_hash(contract_address: str) -> str:
    params = {
        "module": "contract",
        "action": "getcontractcreation",
        "contractaddresses": contract_address,
        "apikey": API_KEY
    }
    response = requests.get(ETHERSCAN_API, params=params).json()
    return response["result"][0]["txHash"]


def get_block_number(tx_hash: str) -> str:
    params = {
        "module": "proxy",
        "action": "eth_getTransactionByHash",
        "txhash": tx_hash,
        "apikey": API_KEY
    }
    response = requests.get(ETHERSCAN_API, params=params).json()
    return response["result"]["blockNumber"]


def get_block_timestamp(block_number: str) -> str:
    params = {
        "module": "proxy",
        "action": "eth_getBlockByNumber",
        "tag": block_number,
        "boolean": "true",
        "apikey": API_KEY
    }
    response = requests.get(ETHERSCAN_API, params=params).json()
    return response["result"]["timestamp"]


def get_creation_block_timestamp(contract_address: str) -> str:
    tx_hash = get_creation_tx_hash(contract_address)
    block_number = get_block_number(tx_hash)
    return get_block_timestamp(block_number)

