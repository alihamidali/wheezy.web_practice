from wheezy.http import WSGIApplication
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory


from urls import all_urls

main = WSGIApplication([
    bootstrap_defaults(url_mapping=all_urls),
    path_routing_middleware_factory
], options)

if __name__ == "__main__":
    from wsgiref.handlers import BaseHandler
    from wsgiref.simpl_server import make_server

    try:
        print('Visit http://localhost:8080/')
        BaseHandler.http_version = '1.1'
        make_server('', 8080, main).serve_forever()
    except KeyboardInterrupt:
        pass
    print('\nThanks')