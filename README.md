# python_grpc_api

Simple examples of gRPC unary server and client

# start
- configure venv (python 3.7)
- install all dependencies from `requirements.txt` file
- run `generate_proto.sh` to generate all necessary gRPC python files based on API definition from `.proto` file

Generated files ends with `pb2.py` and `pb2_grpc.py`

For movie example run `movie_server.py` to launch the server and `movie_client.py` for client

Additionally this repository includes a REST server - `movie_rest.py` for tests comparing gRPC and REST performance:
https://github.com/WojciechGalecki/gatling_rest_vs_grpc_tests
