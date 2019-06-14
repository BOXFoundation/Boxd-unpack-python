#!/usr/bin/env python

from boxd_client.protocol.rpc.boxd_client import BoxdClient


boxd = BoxdClient("39.97.168.26", 19111)
addr = "b1Vc6vBWzjSp71c3c49hx3pENPL1TwU1Exy"


def get_boxdclient():
    return boxd


def get_nonce(addr):
    nonce = boxd.getNonce(addr)
    return nonce


def get_balance(addr):
    return boxd.get_balance(addr)


def view_tx(hash):
    s = boxd.view_tx_detail(hash, spread_split=True)
    print(s)
