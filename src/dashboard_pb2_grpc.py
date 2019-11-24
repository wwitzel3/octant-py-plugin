# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import dashboard_pb2 as dashboard__pb2


class PluginStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Content = channel.unary_unary(
        '/dashboard.Plugin/Content',
        request_serializer=dashboard__pb2.ContentRequest.SerializeToString,
        response_deserializer=dashboard__pb2.ContentResponse.FromString,
        )
    self.HandleAction = channel.unary_unary(
        '/dashboard.Plugin/HandleAction',
        request_serializer=dashboard__pb2.HandleActionRequest.SerializeToString,
        response_deserializer=dashboard__pb2.HandleActionResponse.FromString,
        )
    self.Navigation = channel.unary_unary(
        '/dashboard.Plugin/Navigation',
        request_serializer=dashboard__pb2.NavigationRequest.SerializeToString,
        response_deserializer=dashboard__pb2.NavigationResponse.FromString,
        )
    self.Register = channel.unary_unary(
        '/dashboard.Plugin/Register',
        request_serializer=dashboard__pb2.RegisterRequest.SerializeToString,
        response_deserializer=dashboard__pb2.RegisterResponse.FromString,
        )
    self.Print = channel.unary_unary(
        '/dashboard.Plugin/Print',
        request_serializer=dashboard__pb2.ObjectRequest.SerializeToString,
        response_deserializer=dashboard__pb2.PrintResponse.FromString,
        )
    self.ObjectStatus = channel.unary_unary(
        '/dashboard.Plugin/ObjectStatus',
        request_serializer=dashboard__pb2.ObjectRequest.SerializeToString,
        response_deserializer=dashboard__pb2.ObjectStatusResponse.FromString,
        )
    self.PrintTab = channel.unary_unary(
        '/dashboard.Plugin/PrintTab',
        request_serializer=dashboard__pb2.ObjectRequest.SerializeToString,
        response_deserializer=dashboard__pb2.PrintTabResponse.FromString,
        )
    self.WatchAdd = channel.unary_unary(
        '/dashboard.Plugin/WatchAdd',
        request_serializer=dashboard__pb2.WatchRequest.SerializeToString,
        response_deserializer=dashboard__pb2.Empty.FromString,
        )
    self.WatchUpdate = channel.unary_unary(
        '/dashboard.Plugin/WatchUpdate',
        request_serializer=dashboard__pb2.WatchRequest.SerializeToString,
        response_deserializer=dashboard__pb2.Empty.FromString,
        )
    self.WatchDelete = channel.unary_unary(
        '/dashboard.Plugin/WatchDelete',
        request_serializer=dashboard__pb2.WatchRequest.SerializeToString,
        response_deserializer=dashboard__pb2.Empty.FromString,
        )


class PluginServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Content(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HandleAction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Navigation(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Print(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ObjectStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PrintTab(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchAdd(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WatchDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PluginServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Content': grpc.unary_unary_rpc_method_handler(
          servicer.Content,
          request_deserializer=dashboard__pb2.ContentRequest.FromString,
          response_serializer=dashboard__pb2.ContentResponse.SerializeToString,
      ),
      'HandleAction': grpc.unary_unary_rpc_method_handler(
          servicer.HandleAction,
          request_deserializer=dashboard__pb2.HandleActionRequest.FromString,
          response_serializer=dashboard__pb2.HandleActionResponse.SerializeToString,
      ),
      'Navigation': grpc.unary_unary_rpc_method_handler(
          servicer.Navigation,
          request_deserializer=dashboard__pb2.NavigationRequest.FromString,
          response_serializer=dashboard__pb2.NavigationResponse.SerializeToString,
      ),
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=dashboard__pb2.RegisterRequest.FromString,
          response_serializer=dashboard__pb2.RegisterResponse.SerializeToString,
      ),
      'Print': grpc.unary_unary_rpc_method_handler(
          servicer.Print,
          request_deserializer=dashboard__pb2.ObjectRequest.FromString,
          response_serializer=dashboard__pb2.PrintResponse.SerializeToString,
      ),
      'ObjectStatus': grpc.unary_unary_rpc_method_handler(
          servicer.ObjectStatus,
          request_deserializer=dashboard__pb2.ObjectRequest.FromString,
          response_serializer=dashboard__pb2.ObjectStatusResponse.SerializeToString,
      ),
      'PrintTab': grpc.unary_unary_rpc_method_handler(
          servicer.PrintTab,
          request_deserializer=dashboard__pb2.ObjectRequest.FromString,
          response_serializer=dashboard__pb2.PrintTabResponse.SerializeToString,
      ),
      'WatchAdd': grpc.unary_unary_rpc_method_handler(
          servicer.WatchAdd,
          request_deserializer=dashboard__pb2.WatchRequest.FromString,
          response_serializer=dashboard__pb2.Empty.SerializeToString,
      ),
      'WatchUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.WatchUpdate,
          request_deserializer=dashboard__pb2.WatchRequest.FromString,
          response_serializer=dashboard__pb2.Empty.SerializeToString,
      ),
      'WatchDelete': grpc.unary_unary_rpc_method_handler(
          servicer.WatchDelete,
          request_deserializer=dashboard__pb2.WatchRequest.FromString,
          response_serializer=dashboard__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dashboard.Plugin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
