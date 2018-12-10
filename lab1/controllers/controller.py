from flask import Flask, request

from lab1.core.utils import json_response

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """
    Initializes everything before the first request
    Works similar to post-construct phase in Java
    """
    pass


@app.route('/revert/convert', methods=['POST'])
def revert_and_convert():
    # Extract incoming params from request
    params = request.get_json()

    # Receive string
    string = str(params['string']) if 'string' in params else None
    print('Received string', string, sep=": ", end="\n")

    # Invert string
    try:
        revertedString = string[::-1]
        print('Reverted string', revertedString, sep=": ", end="\n")
    except BaseException:
        response = 'Cannot revert string: ' + str(string)
        return json_response(response)

    # Convert binary string to decimal
    try:
        decimalValue = int(revertedString, 2)
        decimalString = str(decimalValue)
    except BaseException:
        response = 'Cannot convert string: ' + revertedString + " to decimal value"
        return json_response(response)

    print('Decimal value', decimalString, sep=": ", end="\n")

    response = decimalString
    return json_response(response)
