from flask import Flask, request

from lab2.core.utils import json_response

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """
    Initializes everything before the first request
    Works similar to post-construct phase in Java
    """
    pass


@app.route('/', methods=['GET', 'POST', 'HEAD'])
def method():
    # Extract headers from request
    request_dictionary = request.headers

    response = str(request.method) + '\n' + str(request_dictionary)
    print(response)

    return json_response(response)
