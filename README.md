# boxd-unpack-python

Boxd-unpack-python is a python library for working with integrating with clients(Boxd Rpc Node) on the Boxd network.

## Installation

```pip install boxd-client```

## QuickStart

```
from boxd_client.protocol.rpc.boxd_client import BoxdClient
boxd = BoxdClient("39.97.169.1", 19111)

# get current block height
height_resp = boxd.get_block_height()

# get block hash
block_hash_resp = boxd.get_block_hash(height_resp.height)

# get block
block_resp = boxd.get_block(block_hash_resp.hash)
print (block_resp)

```

## Transaction

```
priv_key_hex = "5ace780e4a6e17889a6b8697be6ba902936c148662cce65e6a3153431a1a77c1"
addr = "b1USvtdkLrXXtzTfz8R5tpicJYobDbwuqeT"
fee = 100

to = {}
to["b1Tvej4G8Lma86pgYpWqv4fUFJcEyDdeGst"] = 100

# make transaction
unsigned_tx = boxd.make_unsigned_tx(addr, to, fee)
# sign transaction
signed_tx = boxd.sign_transaction(unsigned_tx.tx, priv_key_hex, unsigned_tx.rawMsgs)
# send transaction
hash = boxd.send_transaction(signed_tx)
```

## Issue Token

```
priv_key_hex = "5ace780e4a6e17889a6b8697be6ba902936c148662cce65e6a3153431a1a77c1"
addr = "b1USvtdkLrXXtzTfz8R5tpicJYobDbwuqeT"
amount = 10000

# issure token
name = "TEST token"
symbol = "TEST"
supply = 10000
decimal = 8
token_tx = boxd.make_unsigned_token_issue_tx(name, symbol, supply, decimal, addr, addr, fee=100)
tx = boxd.sign_transaction(token_tx.tx, priv_key_hex=priv_key_hex, rawMsgs=token_tx.rawMsgs)
hash = boxd.send_transaction(tx)
```

## Create splitAddress

```
priv_key_hex = "5ace780e4a6e17889a6b8697be6ba902936c148662cce65e6a3153431a1a77c1"
addr = "b1USvtdkLrXXtzTfz8R5tpicJYobDbwuqeT"

# create split addr
fee = 100
split_addr_info = {
    "b1k9dMK6xrsXYCBuJfjTN9eTsMCiRb18Hnt": 6,
    "b1g8TPMT4mFZEcDZWomPJWXit4suGHs1eoq": 4
}
split_tx = boxd.make_unsigned_split_addr_tx(addr, split_addr_info, fee)
tx = boxd.sign_transaction(split_tx.tx, priv_key_hex=priv_key_hex, rawMsgs=split_tx.rawMsgs)
hash = boxd.send_transaction(tx)
```



## FQA

### When I run `pip install boxd-client`, I got some errors on `Ubuntu 18.04.1 LTS`.

   Run `sudo apt-get install libsecp256k1-dev` first.

