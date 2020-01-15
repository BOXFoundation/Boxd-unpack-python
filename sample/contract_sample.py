#!/usr/bin/env python

from boxd_client.protocol.rpc.boxd_client import BoxdClient

boxd = BoxdClient("39.97.168.26", 19111)
print(boxd.get_network_id())

addr = "b1ndoQmEd83y4Fza5PzbUQDYpT3mV772J5o"
privKey = "51bbcc29adedb59ef3e99d7f7b390517443dd121cc46424562f79619a642422c"


data = "a74c2bb6"
ret = boxd.do_call("b1USvtdkLrXXtzTfz8R5tpicJYobDbwuqeT", "b5bfzkDvBCx9QvnviesP2FvhFUsqxz8W3ET", data=data)
print(ret)

if __name__ == "__main__":

    pass
