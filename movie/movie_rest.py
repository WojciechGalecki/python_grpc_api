from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/', methods=['POST'])
def rest():
    print(request)
    return Response('{\"movie_id\": \"id from python\"}', status=200, content_type="application/json")


if __name__ == '__main__':
    try:
        app.run(host='localhost', port=3000, threaded=True)
    except KeyboardInterrupt:
        pass
