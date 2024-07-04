from flask_restx import Namespace, Resource

#Create a blueprint for each logical group of routes. This example
# demonstrates how to organize blueprints for hello, user, and product endpoints.

hello_ns = Namespace('hello', description='Just a hello request')

@hello_ns.route('/hello')
class HelloResource(Resource):
    @hello_ns.doc('get_hello')
    def get(self):
        return {"message": "Hello world"}
