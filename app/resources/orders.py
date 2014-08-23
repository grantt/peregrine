import falcon
import json


class OrdersResource(object):
    def on_get(self, req, resp, order_id):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world from order {}!'.format(order_id)

    def on_put(self, req, resp, order_id):
        """Handles PUT requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Error',
                                   ex.message)

        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect.')

        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='utf-8')

    def on_delete(self, req, resp, order_id):
        """Handles DELETE requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Error',
                                   ex.message)

        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect.')

        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='utf-8')

    def on_patch(self, req, resp, order_id):
        """Handles PATCH requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Error',
                                   ex.message)

        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect.')

        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='utf-8')

    def on_options(self, req, resp, order_id):
        """Handles OPTIONS requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Options from order {}!'.format(order_id)


class OrdersCollection(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world from orders!'

    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Error',
                                   ex.message)

        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect.')

        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json, encoding='utf-8')

    def on_options(self, req, resp):
        """Handles OPTIONS requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Options from orders!'

resource = OrdersResource()
collection = OrdersCollection()