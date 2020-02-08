import grpc
from movie import movie_pb2, movie_pb2_grpc
from concurrent import futures


class MovieService(movie_pb2_grpc.MovieServiceServicer):

    def AddMovie(self, request, context):
        print('Received request')
        # logic to perform request
        movie_id = 'from python'

        return movie_pb2.AddMovieResponse(movie_id=movie_id)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServiceServicer_to_server(MovieService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        print('Server running on port: 50051')
        serve()
    except KeyboardInterrupt:
        pass
