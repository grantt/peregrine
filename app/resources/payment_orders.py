import falcon
import json


class PaymentOrdersResource(object):
    def on_get(self, req, resp, order_id):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world from payment orders!'

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


class PaymentOrdersCollection(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Hello world from payment orders!'

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

resource = PaymentOrdersResource()
collection = PaymentOrdersCollection()