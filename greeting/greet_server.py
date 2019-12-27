import logging
import grpc
from greeting import greet_pb2, greet_pb2_grpc
from concurrent import futures


class Greeter(greet_pb2_grpc.GreetServiceServicer):

    def Greet(self, request, context):
        greeting = request.greeting
        return greet_pb2.GreetResponse(result=f'Hello {greeting.firstName} {greeting.lastName} from python')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreetServiceServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print('Server is running...')
    serve()
