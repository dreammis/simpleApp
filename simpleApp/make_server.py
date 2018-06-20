from wsgiref.simple_server import make_server
from wsgiref.headers import Headers
from urllib.parse import parse_qs


import http.client
import re


class Request(object):

    def __init__(self, environ):
        self.environ = environ

    @property
    def args(self):
        get_arguments = parse_qs(self.environ['QUERY_STRING'])
        return {k: v[0] for k, v in get_arguments.items()}

    @property
    def path(self):
        return self.environ['PATH_INFO']


class Response(object):

    def __init__(self, response=None, status=200, charset='utf-8', content_type='text/html'):
        self.response = [] if response is None else response
        self.charset = charset
        self.headers = Headers()
        content_type = "{content_type}; charset={charset}".format(content_type=content_type, charset=charset)
        self.headers.add_header('content_type', content_type)
        self._status = status

    @property
    def status(self):
        status_string = http.client.responses.get(self._status, 'UNKNOWN')
        return "{status} {status_string}".format(status=self._status, status_string=status_string)

    def __iter__(self):
        for val in self.response:
            if isinstance(val, bytes):
                yield val
            else:
                yield val.encode(self.charset)


class NotFoundError(Exception):
    pass



class Router(object):

    def __init__(self):
        self.routing_table = []

    def add_route(self, pattern, callback):
        self.routing_table.append((pattern, callback))

    def match(self, path):
        for (pattern, callback) in self.routing_table:
            m = re.match(pattern, path)
            if m:
                return callback, m.group()
        raise NotFoundError()


def request_response_application(func):
    def application(environ, start_response):
        request = Request(environ)
        response = func(request)
        start_response(response.status, response.headers.items())
        return iter(response)
    return application


@request_response_application
def application(request):
    # import pprint; pprint.pprint(environ)
    name = request.args.get('name')
    return Response(['<h1>malegebide {name}</h1>'.format(name=name)])


if __name__ == "__main__":
    httpd = make_server(host='127.0.0.1', port=999, app=application)
    httpd.serve_forever()

