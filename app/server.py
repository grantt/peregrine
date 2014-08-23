from pulsar.apps import wsgi
from pulsar.apps.wsgi.middleware import middleware_in_executor, wait_for_body_middleware

import config
import routes


class Site(wsgi.LazyWsgi):
    def setup(self, environ=None):
        return wsgi.WsgiHandler(
            [wait_for_body_middleware,
             middleware_in_executor(routes.app)])


def run():
    wsgi.WSGIServer(
        callable=Site(),
        workers=config.worker_count,
        thread_workers=config.thread_worker_count,
        bind=("{}:{}".format(config.host, config.port))).start()

if __name__ == '__main__':
    run()