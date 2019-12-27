import grpc
import logging
from greeting import greet_pb2, greet_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreetServiceStub(channel)
        result = greet_pb2.Greeting()
        result.firstName = 'John'
        result.lastName = 'Doe'
        response = stub.Greet(greet_pb2.GreetRequest(greeting=result))
    print(response.result)


if __name__ == '__main__':
    logging.basicConfig()
    run()
