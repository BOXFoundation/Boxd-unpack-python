# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import boxd_client.protocol.generated.transaction_pb2 as transaction__pb2


class TransactionCommandStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetBalance = channel.unary_unary(
        '/rpcpb.TransactionCommand/GetBalance',
        request_serializer=transaction__pb2.GetBalanceReq.SerializeToString,
        response_deserializer=transaction__pb2.GetBalanceResp.FromString,
        )
    self.GetTokenBalance = channel.unary_unary(
        '/rpcpb.TransactionCommand/GetTokenBalance',
        request_serializer=transaction__pb2.GetTokenBalanceReq.SerializeToString,
        response_deserializer=transaction__pb2.GetBalanceResp.FromString,
        )
    self.FetchUtxos = channel.unary_unary(
        '/rpcpb.TransactionCommand/FetchUtxos',
        request_serializer=transaction__pb2.FetchUtxosReq.SerializeToString,
        response_deserializer=transaction__pb2.FetchUtxosResp.FromString,
        )
    self.SendTransaction = channel.unary_unary(
        '/rpcpb.TransactionCommand/SendTransaction',
        request_serializer=transaction__pb2.SendTransactionReq.SerializeToString,
        response_deserializer=transaction__pb2.SendTransactionResp.FromString,
        )
    self.GetRawTransaction = channel.unary_unary(
        '/rpcpb.TransactionCommand/GetRawTransaction',
        request_serializer=transaction__pb2.GetRawTransactionRequest.SerializeToString,
        response_deserializer=transaction__pb2.GetRawTransactionResponse.FromString,
        )
    self.GetFeePrice = channel.unary_unary(
        '/rpcpb.TransactionCommand/GetFeePrice',
        request_serializer=transaction__pb2.GetFeePriceRequest.SerializeToString,
        response_deserializer=transaction__pb2.GetFeePriceResponse.FromString,
        )
    self.MakeUnsignedTx = channel.unary_unary(
        '/rpcpb.TransactionCommand/MakeUnsignedTx',
        request_serializer=transaction__pb2.MakeTxReq.SerializeToString,
        response_deserializer=transaction__pb2.MakeTxResp.FromString,
        )
    self.MakeUnsignedSplitAddrTx = channel.unary_unary(
        '/rpcpb.TransactionCommand/MakeUnsignedSplitAddrTx',
        request_serializer=transaction__pb2.MakeSplitAddrTxReq.SerializeToString,
        response_deserializer=transaction__pb2.MakeSplitAddrTxResp.FromString,
        )
    self.MakeUnsignedTokenIssueTx = channel.unary_unary(
        '/rpcpb.TransactionCommand/MakeUnsignedTokenIssueTx',
        request_serializer=transaction__pb2.MakeTokenIssueTxReq.SerializeToString,
        response_deserializer=transaction__pb2.MakeTokenIssueTxResp.FromString,
        )
    self.SendRawTransaction = channel.unary_unary(
        '/rpcpb.TransactionCommand/SendRawTransaction',
        request_serializer=transaction__pb2.SendRawTransactionReq.SerializeToString,
        response_deserializer=transaction__pb2.SendTransactionResp.FromString,
        )
    self.MakeUnsignedTokenTransferTx = channel.unary_unary(
        '/rpcpb.TransactionCommand/MakeUnsignedTokenTransferTx',
        request_serializer=transaction__pb2.MakeTokenTransferTxReq.SerializeToString,
        response_deserializer=transaction__pb2.MakeTxResp.FromString,
        )


class TransactionCommandServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetBalance(self, request, context):
    """rpc GetBalance (GetBalanceReq) returns (GetBalanceResp) {
    option (google.api.http) = {
    post: "/v1/tx/getbalance"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTokenBalance(self, request, context):
    """rpc GetTokenBalance (GetTokenBalanceReq) returns (GetBalanceResp) {
    option (google.api.http) = {
    post: "/v1/tx/gettokenbalance"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchUtxos(self, request, context):
    """rpc FetchUtxos (FetchUtxosReq) returns (FetchUtxosResp) {
    option (google.api.http) = {
    post: "/v1/tx/fetchutxos"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendTransaction(self, request, context):
    """rpc SendTransaction (SendTransactionReq) returns (SendTransactionResp) {
    option (google.api.http) = {
    post: "/v1/tx/sendtransaction"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRawTransaction(self, request, context):
    """rpc GetRawTransaction (GetRawTransactionRequest) returns (GetRawTransactionResponse) {
    option (google.api.http) = {
    post: "/v1/tx/getrawtransaction"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeePrice(self, request, context):
    """rpc GetFeePrice (GetFeePriceRequest) returns (GetFeePriceResponse) {
    option (google.api.http) = {
    post: "/v1/tx/getfeeprice"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MakeUnsignedTx(self, request, context):
    """rpc MakeUnsignedTx (MakeTxReq) returns (MakeTxResp) {
    option (google.api.http) = {
    post: "/v1/tx/makeunsignedtx"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MakeUnsignedSplitAddrTx(self, request, context):
    """rpc MakeUnsignedSplitAddrTx (MakeSplitAddrTxReq) returns (MakeSplitAddrTxResp) {
    option (google.api.http) = {
    post: "/v1/tx/makeunsignedtx/splitaddr"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MakeUnsignedTokenIssueTx(self, request, context):
    """rpc MakeUnsignedTokenIssueTx (MakeTokenIssueTxReq) returns (MakeTokenIssueTxResp) {
    option (google.api.http) = {
    post: "/v1/tx/makeunsignedtx/token/issue"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendRawTransaction(self, request, context):
    """rpc SendRawTransaction (SendRawTransactionReq) returns (SendTransactionResp) {
    option (google.api.http) = {
    post: "/v1/tx/sendrawtransaction"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MakeUnsignedTokenTransferTx(self, request, context):
    """rpc MakeUnsignedTokenTransferTx (MakeTokenTransferTxReq) returns (MakeTxResp) {
    option (google.api.http) = {
    post: "/v1/tx/makeunsignedtx/token/transfer"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransactionCommandServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetBalance,
          request_deserializer=transaction__pb2.GetBalanceReq.FromString,
          response_serializer=transaction__pb2.GetBalanceResp.SerializeToString,
      ),
      'GetTokenBalance': grpc.unary_unary_rpc_method_handler(
          servicer.GetTokenBalance,
          request_deserializer=transaction__pb2.GetTokenBalanceReq.FromString,
          response_serializer=transaction__pb2.GetBalanceResp.SerializeToString,
      ),
      'FetchUtxos': grpc.unary_unary_rpc_method_handler(
          servicer.FetchUtxos,
          request_deserializer=transaction__pb2.FetchUtxosReq.FromString,
          response_serializer=transaction__pb2.FetchUtxosResp.SerializeToString,
      ),
      'SendTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.SendTransaction,
          request_deserializer=transaction__pb2.SendTransactionReq.FromString,
          response_serializer=transaction__pb2.SendTransactionResp.SerializeToString,
      ),
      'GetRawTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.GetRawTransaction,
          request_deserializer=transaction__pb2.GetRawTransactionRequest.FromString,
          response_serializer=transaction__pb2.GetRawTransactionResponse.SerializeToString,
      ),
      'GetFeePrice': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeePrice,
          request_deserializer=transaction__pb2.GetFeePriceRequest.FromString,
          response_serializer=transaction__pb2.GetFeePriceResponse.SerializeToString,
      ),
      'MakeUnsignedTx': grpc.unary_unary_rpc_method_handler(
          servicer.MakeUnsignedTx,
          request_deserializer=transaction__pb2.MakeTxReq.FromString,
          response_serializer=transaction__pb2.MakeTxResp.SerializeToString,
      ),
      'MakeUnsignedSplitAddrTx': grpc.unary_unary_rpc_method_handler(
          servicer.MakeUnsignedSplitAddrTx,
          request_deserializer=transaction__pb2.MakeSplitAddrTxReq.FromString,
          response_serializer=transaction__pb2.MakeSplitAddrTxResp.SerializeToString,
      ),
      'MakeUnsignedTokenIssueTx': grpc.unary_unary_rpc_method_handler(
          servicer.MakeUnsignedTokenIssueTx,
          request_deserializer=transaction__pb2.MakeTokenIssueTxReq.FromString,
          response_serializer=transaction__pb2.MakeTokenIssueTxResp.SerializeToString,
      ),
      'SendRawTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.SendRawTransaction,
          request_deserializer=transaction__pb2.SendRawTransactionReq.FromString,
          response_serializer=transaction__pb2.SendTransactionResp.SerializeToString,
      ),
      'MakeUnsignedTokenTransferTx': grpc.unary_unary_rpc_method_handler(
          servicer.MakeUnsignedTokenTransferTx,
          request_deserializer=transaction__pb2.MakeTokenTransferTxReq.FromString,
          response_serializer=transaction__pb2.MakeTxResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rpcpb.TransactionCommand', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
