from boxd_client.protocol.rpc.boxd_client import BoxdClient
# from sample.Sample_helper import view_tx

abi = [
    {
        "constant": False,
        "inputs": [],
        "name": "getAAA",
        "outputs": [
            {
                "name": "",
                "type": "string[]"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_u",
                "type": "uint256"
            }
        ],
        "name": "getData",
        "outputs": [
            {
                "name": "",
                "type": "uint256[]"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "getStu",
        "outputs": [
            {
                "components": [
                    {
                        "name": "name",
                        "type": "string"
                    },
                    {
                        "name": "addr",
                        "type": "address"
                    },
                    {
                        "name": "u",
                        "type": "uint256"
                    }
                ],
                "name": "",
                "type": "tuple"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "s",
                "type": "string"
            }
        ],
        "name": "setGreet",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "u",
                "type": "uint256"
            }
        ],
        "name": "e",
        "type": "event"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "aaa",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "addr",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "data",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getAddr",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "a",
                "type": "uint256"
            },
            {
                "name": "b",
                "type": "uint256"
            }
        ],
        "name": "getMax",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "greet",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "greeting",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_u",
                "type": "uint256[]"
            }
        ],
        "name": "setData",
        "outputs": [
            {
                "name": "t",
                "type": "uint256[]"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "u",
                "type": "bytes31[2]"
            }
        ],
        "name": "setSimpleData",
        "outputs": [
            {
                "name": "",
                "type": "bytes31[2]"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "t",
                "type": "uint256"
            }
        ],
        "name": "test",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "t",
                "type": "int256"
            }
        ],
        "name": "test",
        "outputs": [
            {
                "name": "",
                "type": "int256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "test",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "pure",
        "type": "function"
    }
]

bin = "608060405234801561001057600080fd5b50611355806100206000396000f3fe6080604052600436106100e0576000357c0100000000000000000000000000000000000000000000000000000000900480630178fe3f146100e557806326b230201461012257806329e99f071461015f5780632d3085f61461019c578063624c6056146101c7578063767800de146102045780639698086b1461022f5780639b22c05d14610258578063a74c2bb614610295578063c87cfe63146102c0578063cfae3217146102fd578063e7ee190e14610328578063ef690cc014610365578063f0ba844014610390578063f7660610146103cd578063f8a8fd6d146103f8575b600080fd5b3480156100f157600080fd5b5061010c60048036036101079190810190610d6a565b610423565b6040516101199190611033565b60405180910390f35b34801561012e57600080fd5b5061014960048036036101449190810190610d93565b6104a9565b60405161015691906110d6565b60405180910390f35b34801561016b57600080fd5b5061018660048036036101819190810190610d6a565b6104bd565b60405161019391906110d6565b60405180910390f35b3480156101a857600080fd5b506101b16104c8565b6040516101be9190611011565b60405180910390f35b3480156101d357600080fd5b506101ee60048036036101e99190810190610c96565b610691565b6040516101fb9190610ff6565b60405180910390f35b34801561021057600080fd5b506102196106a1565b6040516102269190610fdb565b60405180910390f35b34801561023b57600080fd5b5061025660048036036102519190810190610d29565b6106c7565b005b34801561026457600080fd5b5061027f600480360361027a9190810190610d00565b6106e1565b60405161028c9190611055565b60405180910390f35b3480156102a157600080fd5b506102aa6106eb565b6040516102b79190610fdb565b60405180910390f35b3480156102cc57600080fd5b506102e760048036036102e29190810190610cbf565b6106f3565b6040516102f49190611033565b60405180910390f35b34801561030957600080fd5b506103126106fd565b60405161031f9190611092565b60405180910390f35b34801561033457600080fd5b5061034f600480360361034a9190810190610d6a565b61079f565b60405161035c9190611070565b60405180910390f35b34801561037157600080fd5b5061037a61085a565b6040516103879190611070565b60405180910390f35b34801561039c57600080fd5b506103b760048036036103b29190810190610d6a565b6108f8565b6040516103c491906110d6565b60405180910390f35b3480156103d957600080fd5b506103e261091b565b6040516103ef91906110b4565b60405180910390f35b34801561040457600080fd5b5061040d6109b3565b60405161041a9190611092565b60405180910390f35b60606003829080600181540180825580915050906001820390600052602060002001600090919290919091505550600380548060200260200160405190810160405280929190818152602001828054801561049d57602002820191906000526020600020905b815481526020019060010190808311610489575b50505050509050919050565b60006104b583836109f0565b905092915050565b600060649050919050565b606060028060018154018082558091505090600182039060005260206000200160006040805190810160405280600181526020017f610000000000000000000000000000000000000000000000000000000000000081525090919091509080519060200190610538929190610a0a565b505060028060018154018082558091505090600182039060005260206000200160006040805190810160405280600181526020017f6200000000000000000000000000000000000000000000000000000000000000815250909190915090805190602001906105a8929190610a0a565b50506002805480602002602001604051908101604052809291908181526020016000905b82821015610688578382906000526020600020018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156106745780601f1061064957610100808354040283529160200191610674565b820191906000526020600020905b81548152906001019060200180831161065757829003601f168201915b5050505050815260200190600101906105cc565b50505050905090565b610699610a8a565b819050919050565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b80600090805190602001906106dd929190610a0a565b5050565b6000819050919050565b600080905090565b6060819050919050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156107955780601f1061076a57610100808354040283529160200191610795565b820191906000526020600020905b81548152906001019060200180831161077857829003601f168201915b5050505050905090565b6002818154811015156107ae57fe5b906000526020600020016000915090508054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156108525780601f1061082757610100808354040283529160200191610852565b820191906000526020600020905b81548152906001019060200180831161083557829003601f168201915b505050505081565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156108f05780601f106108c5576101008083540402835291602001916108f0565b820191906000526020600020905b8154815290600101906020018083116108d357829003601f168201915b505050505081565b60038181548110151561090757fe5b906000526020600020016000915090505481565b610923610aac565b61092b610aac565b6040805190810160405280600381526020017f6161610000000000000000000000000000000000000000000000000000000000815250816000018190525033816020019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff168152505060648160400181815250508091505090565b60606040805190810160405280600381526020017f6564660000000000000000000000000000000000000000000000000000000000815250905090565b600081831015610a005781610a02565b825b905092915050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610a4b57805160ff1916838001178555610a79565b82800160010185558215610a79579182015b82811115610a78578251825591602001919060010190610a5d565b5b509050610a869190610ae4565b5090565b6040805190810160405280600290602082028038833980820191505090505090565b60606040519081016040528060608152602001600073ffffffffffffffffffffffffffffffffffffffff168152602001600081525090565b610b0691905b80821115610b02576000816000905550600101610aea565b5090565b90565b600082601f8301121515610b1c57600080fd5b6002610b2f610b2a8261111e565b6110f1565b91508183856020840282011115610b4557600080fd5b60005b83811015610b755781610b5b8882610c04565b845260208401935060208301925050600181019050610b48565b5050505092915050565b600082601f8301121515610b9257600080fd5b8135610ba5610ba082611140565b6110f1565b91508181835260208401935060208101905083856020840282011115610bca57600080fd5b60005b83811015610bfa5781610be08882610c82565b845260208401935060208301925050600181019050610bcd565b5050505092915050565b6000610c108235611288565b905092915050565b6000610c2482356112b4565b905092915050565b600082601f8301121515610c3f57600080fd5b8135610c52610c4d82611168565b6110f1565b91508082526020830160208301858383011115610c6e57600080fd5b610c798382846112c8565b50505092915050565b6000610c8e82356112be565b905092915050565b600060408284031215610ca857600080fd5b6000610cb684828501610b09565b91505092915050565b600060208284031215610cd157600080fd5b600082013567ffffffffffffffff811115610ceb57600080fd5b610cf784828501610b7f565b91505092915050565b600060208284031215610d1257600080fd5b6000610d2084828501610c18565b91505092915050565b600060208284031215610d3b57600080fd5b600082013567ffffffffffffffff811115610d5557600080fd5b610d6184828501610c2c565b91505092915050565b600060208284031215610d7c57600080fd5b6000610d8a84828501610c82565b91505092915050565b60008060408385031215610da657600080fd5b6000610db485828601610c82565b9250506020610dc585828601610c82565b9150509250929050565b610dd881611216565b82525050565b610de7816111b8565b610df082611194565b60005b82811015610e2257610e06858351610ef2565b610e0f826111ef565b9150602085019450600181019050610df3565b5050505050565b6000610e34826111c3565b80845260208401935083602082028501610e4d8561119e565b60005b84811015610e86578383038852610e68838351610f46565b9250610e73826111fc565b9150602088019750600181019050610e50565b508196508694505050505092915050565b6000610ea2826111ce565b808452602084019350610eb4836111ab565b60005b82811015610ee657610eca868351610fcc565b610ed382611209565b9150602086019550600181019050610eb7565b50849250505092915050565b610efb81611228565b82525050565b610f0a81611254565b82525050565b6000610f1b826111e4565b808452610f2f8160208601602086016112d7565b610f388161130a565b602085010191505092915050565b6000610f51826111d9565b808452610f658160208601602086016112d7565b610f6e8161130a565b602085010191505092915050565b60006060830160008301518482036000860152610f998282610f46565b9150506020830151610fae6020860182610dcf565b506040830151610fc16040860182610fcc565b508091505092915050565b610fd58161127e565b82525050565b6000602082019050610ff06000830184610dcf565b92915050565b600060408201905061100b6000830184610dde565b92915050565b6000602082019050818103600083015261102b8184610e29565b905092915050565b6000602082019050818103600083015261104d8184610e97565b905092915050565b600060208201905061106a6000830184610f01565b92915050565b6000602082019050818103600083015261108a8184610f46565b905092915050565b600060208201905081810360008301526110ac8184610f10565b905092915050565b600060208201905081810360008301526110ce8184610f7c565b905092915050565b60006020820190506110eb6000830184610fcc565b92915050565b6000604051905081810181811067ffffffffffffffff8211171561111457600080fd5b8060405250919050565b600067ffffffffffffffff82111561113557600080fd5b602082029050919050565b600067ffffffffffffffff82111561115757600080fd5b602082029050602081019050919050565b600067ffffffffffffffff82111561117f57600080fd5b601f19601f8301169050602081019050919050565b6000819050919050565b6000602082019050919050565b6000602082019050919050565b600060029050919050565b600081519050919050565b600081519050919050565b600081519050919050565b600081519050919050565b6000602082019050919050565b6000602082019050919050565b6000602082019050919050565b60006112218261125e565b9050919050565b60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0082169050919050565b6000819050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b60007fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0082169050919050565b6000819050919050565b6000819050919050565b82818337600083830152505050565b60005b838110156112f55780820151818401526020810190506112da565b83811115611304576000848401525b50505050565b6000601f19601f830116905091905056fea265627a7a723058204651e6198f4f66c34e9d0c6c7881695d1bb277762729ba21c723bf5132b04a1b6c6578706572696d656e74616cf50037"


priv_key_hex = "5ace780e4a6e17889a6b8697be6ba902936c148662cce65e6a3153431a1a77c1"
from_address = "b1USvtdkLrXXtzTfz8R5tpicJYobDbwuqeT"


# private static String RPC_HOST = "39.97.168.26";
# private static int RPC_PORT = 19111;

#
# private static String RPC_HOST = "192.168.21.52";
# private static int RPC_PORT = 19191;


boxd = BoxdClient(host="192.168.21.52", port=19191)
# boxd = BoxdClient(host="39.97.168.26", port=19111)

contract_address = "b5qX4ERqHSkotLDFy5RsCFp4qjyYHaBk5dW"

if contract_address is None or contract_address == "":
    demo = boxd.contract(from_address, abi=abi, bytecode=bin)

    # deploy
    tx_hash = demo.constructor().transact()
    print(tx_hash)
else:
    demo = boxd.contract(from_address, contract_address, abi=abi)
    # # print(demo.functions.test(10).call())
    print(demo.functions.getAddr().call())
    print(demo.functions.greet().call())

    tx_hash = demo.functions.setGreet("Jarvis").transact()
    print(tx_hash)





