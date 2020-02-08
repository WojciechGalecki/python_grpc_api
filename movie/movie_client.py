import grpc
from movie import movie_pb2, movie_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = movie_pb2_grpc.MovieServiceStub(channel)

        movie = movie_pb2.Movie()
        movie.title = 'Goodfellas'

        response = stub.AddMovie(movie)

    print(response.movie_id)


if __name__ == '__main__':
    run()





