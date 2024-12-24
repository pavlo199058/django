from web3 import Web3

# Ganache Testnet
ganache_mode = True

ganache_url = "HTTP://127.0.0.1:8545"

# infura apikey
infura_apikey = "apikey" 
infura_url= f"https://mainnet.infura.io/v3/{infura_apikey}"


# Public key & Private key accounts
victim_address = "0x5f5507c34c960c17823f1fc409e0b4e968432870" # The victim's ETH address
victim_key = "0xededa8a37f2b165a636fd0bb0f34805abb3a2955f0bdd1bd8c8c283acce680c2" # The victim's private key
# victim_key = "0xb3f705b056db61abc2ff0a8256380ae8d6b26b151eca575d63e37dcd39e8be5c" # The victim's private key
# victim_key = "0x809d2127462364a7f1258e45a1d359de2854acebf41aa8379884d8f5f3bcf8ec" # The victim's private key


recipient_address = "0x391EB861c5EBa3578CBf6237db946C1c03c32BD6" # An account you want to send ETH to
