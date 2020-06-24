from functools import wraps
from flask import request, send_from_directory


def with_static(static_file_name=None):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            file_name = static_file_name
            if file_name is None:
                file_name = request.endpoint.replace('.', '/') + '.html'
            res = func(*args, **kwargs)
            if res is None:
                res = {}
            elif not isinstance(res, dict):
                return res
            return send_from_directory('static', file_name), res

        return decorated_function

    return decorator
