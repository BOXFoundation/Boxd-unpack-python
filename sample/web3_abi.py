from eth_abi import  encode_single, encode_abi
from boxd_client.util.hexadecimal import bytes_to_hex


# encode abi

r = encode_single('uint256', 12345)
print(bytes_to_hex(r))


r = encode_abi(['bytes32', 'bytes32'], [b'a', b'b'])
print(bytes_to_hex(r))