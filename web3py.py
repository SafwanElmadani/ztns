from web3 import Web3
import numpy as numpy
import json

ganache_url = 'HTTP://127.0.0.1:7545'

w3 = Web3(Web3.HTTPProvider(ganache_url))

#got these informations from ganache
acc1 = '0xea5677F9319B9dA49f4B4c4227eD7af72c4a692d'
private_key = '07c58c823257c5f3dc732acf24bf27ae1e292cba9109305738ad03baa8c9453d'

#this is the contract address
address_cont1 = '0x112FB347B493Eb7504440E63863375B4CCb4e27C'

print(w3.isConnected())
print(w3.isAddress(acc1))

#get account address
w3.eth._get_accounts()[0]


with open('/home/safwan/Documents/school_files/blockchain/smart-contract/projects/zta/build/contracts/nsdp.json') as f:
    data = json.load(f)

#data['abi']

valid_address = w3.toChecksumAddress(address_cont1)

contract_instance = w3.eth.contract(address=valid_address,
                                    abi= data['abi'])

contract_instance.functions.peopleCount().call()

add_people = contract_instance.functions.addPerson("saf", "atibm").build_transaction(
        {
            "gasPrice": w3.eth.gas_price,
            "chainId": 1337,
            "from": acc1,
            "nonce": 0
        })

signed_transaction = w3.eth.account.sign_transaction(add_people,
                                                     private_key=private_key)

sendtransaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

transaction_reciept = w3.eth.wait_for_transaction_receipt(sendtransaction_hash)

