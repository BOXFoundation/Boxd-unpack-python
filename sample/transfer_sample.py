#!/usr/bin/env python

import time

from boxd_client.protocol.rpc.boxd_client import BoxdClient
from boxd_client.util.hexadecimal import bytes_to_hex

boxd = BoxdClient("39.97.169.1", 19111)

priv_key_hex = "5ace780e4a6e17889a6b8697be6ba902936c148662cce65e6a3153431a1a77c1"
addr = "b1USvtdkLrXXtzTfz8R5tpicJYobDbwuqeT"
amount = 700
fee = 100

to = {}
to["b1Tvej4G8Lma86pgYpWqv4fUFJcEyDdeGst"] = 100
# to["b1USvtdkLrXXtzTfz8R5tpicJYobDbwuqeT"] = 200
to["b1dSx5FTXEpzB7hWZAydY5N4A5PtFJb57V1"] = 200
to["b1Vc6vBWzjSp71c3c49hx3pENPL1TwU1Exy"] = 300

boxd.faucet(addr, amount)
time.sleep(3)


def send_transaction(addr, to, fee):
    unsigned_tx = boxd.make_unsigned_tx(addr, to, fee)
    print("unsigned:")
    print(unsigned_tx)
    signed_tx = boxd.sign_transaction(unsigned_tx.tx, priv_key_hex, unsigned_tx.rawMsgs)
    print("signed:")
    print(signed_tx)
    print(bytes_to_hex(signed_tx.SerializeToString()))
    hash = boxd.send_transaction(signed_tx)
    return hash


def get_raw_tx(addr, to, fee):
    unsigned_tx = boxd.make_unsigned_tx(addr, to, fee)
    signed_tx = boxd.sign_transaction(unsigned_tx.tx, priv_key_hex, unsigned_tx.rawMsgs)
    return bytes_to_hex(signed_tx.SerializeToString())


def send_raw_transaction(raw_tx):
    return boxd.send_raw_transaction(raw_tx)


def send_offline_signed_transaction(addr, to, fee):
    balance = boxd.get_balance(addr)
    print(balance)
    if balance[addr] < amount + fee:
        print("low balance")
        sys.exit(0)

    utxos = boxd.fetch_utxos(addr, amount)
    print("\nuntxos:")
    print(utxos)

    unsigned_tx = boxd.create_raw_transaction(addr, utxos, to, fee)
    print("\nunsigned_tx:")
    print(unsigned_tx)

    signed_tx = boxd.sign_transaction(unsigned_tx, priv_key_hex)
    print("\nsigned_tx:")
    print(signed_tx)
    print(bytes_to_hex(signed_tx.SerializeToString()))

    return boxd.send_transaction(signed_tx)


def view_tx(hash):
    tx_detail = boxd.view_tx_detail(hash, False)
    print(tx_detail)



if __name__ == "__main__":

    # hash = send_transaction(addr, to, fee)
    # time.sleep(1)
    # view_tx(hash)

    raw_tx = get_raw_tx(addr, to, fee)
    raw_tx_hash = send_raw_transaction(raw_tx)
    time.sleep(1)
    view_tx(raw_tx_hash)
