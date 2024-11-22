from web3 import Web3

# Ganache Testnet
ganache_mode = True

ganache_url = "HTTP://127.0.0.1:8545"

# infura apikey
infura_apikey = "apikey" 
infura_url= f"https://mainnet.infura.io/v3/{infura_apikey}"


# Public key & Private key accounts
victim_address = "0x5f5507c34c960c17823f1fc409e0b4e968432870" # The victim's ETH address
victim_key = "a75401b397e42ec37aae9a974883ede9eea02dbc9981633f3cce4c67dbd60302" # The victim's private key


recipient_address = "0x391EB861c5EBa3578CBf6237db946C1c03c32BD6" # An account you want to send ETH to
