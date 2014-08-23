import falcon
from resources import orders

app = api = falcon.API()

api.add_route('/orders', orders.resource)