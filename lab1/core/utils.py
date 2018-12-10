import calendar
import datetime

from flask import make_response

JSON_MIME_TYPE = 'application/json'


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)


def datetime_to_timestamp(date_time: datetime):
    return str(calendar.timegm(date_time.timetuple()))
