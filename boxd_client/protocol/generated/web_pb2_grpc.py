# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import boxd_client.protocol.generated.web_pb2 as web__pb2


class WebApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ViewTxDetail = channel.unary_unary(
        '/rpcpb.WebApi/ViewTxDetail',
        request_serializer=web__pb2.ViewTxDetailReq.SerializeToString,
        response_deserializer=web__pb2.ViewTxDetailResp.FromString,
        )
    self.ViewBlockDetail = channel.unary_unary(
        '/rpcpb.WebApi/ViewBlockDetail',
        request_serializer=web__pb2.ViewBlockDetailReq.SerializeToString,
        response_deserializer=web__pb2.ViewBlockDetailResp.FromString,
        )
    self.ListenAndReadNewBlock = channel.unary_stream(
        '/rpcpb.WebApi/ListenAndReadNewBlock',
        request_serializer=web__pb2.ListenBlocksReq.SerializeToString,
        response_deserializer=web__pb2.BlockDetail.FromString,
        )


class WebApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ViewTxDetail(self, request, context):
    """rpc ViewTxDetail (ViewTxDetailReq) returns (ViewTxDetailResp) {
    option (google.api.http) = {
    post: "/v1/tx/detail"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ViewBlockDetail(self, request, context):
    """rpc ViewBlockDetail (ViewBlockDetailReq) returns (ViewBlockDetailResp) {
    option (google.api.http) = {
    post: "/v1/block/detail"
    body: "*"
    };
    }
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListenAndReadNewBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WebApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ViewTxDetail': grpc.unary_unary_rpc_method_handler(
          servicer.ViewTxDetail,
          request_deserializer=web__pb2.ViewTxDetailReq.FromString,
          response_serializer=web__pb2.ViewTxDetailResp.SerializeToString,
      ),
      'ViewBlockDetail': grpc.unary_unary_rpc_method_handler(
          servicer.ViewBlockDetail,
          request_deserializer=web__pb2.ViewBlockDetailReq.FromString,
          response_serializer=web__pb2.ViewBlockDetailResp.SerializeToString,
      ),
      'ListenAndReadNewBlock': grpc.unary_stream_rpc_method_handler(
          servicer.ListenAndReadNewBlock,
          request_deserializer=web__pb2.ListenBlocksReq.FromString,
          response_serializer=web__pb2.BlockDetail.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rpcpb.WebApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
