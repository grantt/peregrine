import falcon
from resources import orders, payment_orders

app = api = falcon.API()

api.add_route('/orders/{order_id}', orders.resource)
api.add_route('/orders', orders.collection)

api.add_route('/payment/order/{order_id}', payment_orders.collection)
api.add_route('/payment/orders', payment_orders.collection)