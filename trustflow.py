from web3 import Web3
import numpy as numpy
import json

"""
This script is used to interact with nsdp smart contract.
Integers and numbers with demimal numbers must be multiplied by 10000 
and received values need to be divided by 10000.
"""

ganache_url = 'HTTP://127.0.0.1:7545'

w3 = Web3(Web3.HTTPProvider(ganache_url))

#got these informations from ganache
account_from = {
        'acc0' : '0x09Dce836adf7d3a712F4ef74c5B7D845FDFEDd36',
        'private_key' : 'bdbb97799b200c0b8909064895803ea9b258022f9bd1c0aeeb61f741e99643c4'
        }

#this is the contract address
#account_to = '0x112FB347B493Eb7504440E63863375B4CCb4e27C'
account_to = input('Enter contract address:')

print(w3.isConnected())

print(w3.isAddress(account_from["acc0"]))

#get account address
accounts_on_blockchain = w3.eth._get_accounts()

#load contract's abi
with open('/home/safwan/Documents/school_files/blockchain/smart-contract/projects/zta/build/contracts/nsdp.json') as f:
    data = json.load(f)
valid_address = w3.toChecksumAddress(account_to)
contract_instance = w3.eth.contract(address=valid_address, abi= data['abi'])

#get threshold value
contract_instance.functions.threshold().call()

def check_account_exists(address_to_check):
    return contract_instance.functions.entities(w3.toChecksumAddress(address_to_check)).call()[-1]


def add_new_entity(address_to_add, trust_value, account_from):
    nonce = w3.eth.getTransactionCount(w3.toChecksumAddress(account_from['acc0']))
    #build transaction 
    trust_value = int(trust_value*10000)
    add_entities = contract_instance.functions.create_new_entity(w3.toChecksumAddress(address_to_add), (trust_value)).buildTransaction({
                'nonce': nonce,
                'from':w3.toChecksumAddress(account_from['acc0']),
                #'to': account_to, cannot be set
                'chainId': 1337, #for truffle
                'gasPrice': w3.eth.gasPrice
            })
            
    #sign transaction
    signed_transaction = w3.eth.account.sign_transaction(add_entities, private_key=account_from['private_key'])
    #send transaction
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    #get transaction hash
    transaction_reciept = w3.eth.wait_for_transaction_receipt(transaction_hash)
    return transaction_hash, transaction_reciept

def update_trust_value(address_to_update, new_trust_value, account_from):
    if not check_account_exists(address_to_update):
        return 'account does not exist'
    nonce = w3.eth.getTransactionCount(w3.toChecksumAddress(account_from['acc0']))
    #build transaction
    new_trust_value = int(new_trust_value*10000)
    update_trustvalue = contract_instance.functions.update_trust_value(w3.toChecksumAddress(address_to_update), new_trust_value).buildTransaction({
                'nonce': nonce,
                'from':w3.toChecksumAddress(account_from['acc0']),
                #'to': account_to, cannot be set
                'chainId': 1337, #for truffle
                'gasPrice': w3.eth.gasPrice
            })

    #sign transaction
    signed_transaction = w3.eth.account.sign_transaction(update_trustvalue, private_key=account_from['private_key'])
    #send transaction
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    #get transaction hash
    transaction_reciept = w3.eth.wait_for_transaction_receipt(transaction_hash)
    return transaction_hash, transaction_reciept

def add_accounts(accounts,trust_value,account_from):
    """
    add account(s) from a list.
    accounts: list of accounts to add
    account_from: the account that will be used to send the transaction
    """
    #add accounts to the smart contract here
    for i in accounts:
        #do nothing if the accout is already added
        if check_account_exists(i):
            continue
        add_new_entity(i,trust_value,account_from)

def get_trust_value(address):
    """
    get trust value for <address>
    """
    if check_account_exists(address):
        return (contract_instance.functions.get_trust_value(w3.toChecksumAddress(address)).call())/10000
    else:
        return 'account does not exist'



def update_threshold(new_threshold,account_from):
    nonce = w3.eth.getTransactionCount(w3.toChecksumAddress(account_from['acc0']))
    #build transaction
    new_threshold = int(new_threshold*10000)
    update_transaction = contract_instance.functions.update_threshold(new_threshold).buildTransaction({
                'nonce': nonce,
                'from':w3.toChecksumAddress(account_from['acc0']),
                #'to': account_to, cannot be set
                'chainId': 1337, #for truffle
                'gasPrice': w3.eth.gasPrice
            })

    #sign transaction
    signed_transaction = w3.eth.account.sign_transaction(update_transaction, private_key=account_from['private_key'])
    #send transaction
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    #get transaction hash
    transaction_reciept = w3.eth.wait_for_transaction_receipt(transaction_hash)
    return transaction_hash, transaction_reciept
