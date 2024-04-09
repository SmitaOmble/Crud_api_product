from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from flask_restful_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from database import Product


app = Flask(__name__)
# api = Api(app)
api = swagger.docs(Api(app), apiVersion='1.0', api_spec_url='/docs')  # Add Swagger documentation endpoint

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"


@app.route('/index')
def index():
    return 'Welcome to the Product API'


swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product_details.db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)


product_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'price': fields.Float,
    'rating': fields.Float,
    'stock': fields.Integer,
    'brand': fields.String,
    'category': fields.String,
}

product_parser = reqparse.RequestParser()
product_parser.add_argument('title', type=str, required=True, help='Title is required')
product_parser.add_argument('description', type=str, required=False)
product_parser.add_argument('price', type=float, required=True, help='Price is required')
product_parser.add_argument('rating', type=float, required=True, help='Rating is required')
product_parser.add_argument('stock', type=int, required=True, help='Stock is required')
product_parser.add_argument('brand', type=str, required=True, help='Brand is required')
product_parser.add_argument('category', type=str, required=True, help='Category is required')


class ProductList(Resource):
    @marshal_with(product_fields)
    def get(self, id=None):
        if id is not None:
            product = Product.query.filter_by(id=id).first()
            if product:
                return product, 200
            else:
                return {'message': 'Product not found'}, 404
        else:
            return Product.query.all(), 200  # Changed status code to 200 for successful GET all products

    def post(self):
        try:
            args = product_parser.parse_args()
            args.pop('id', None)
            product = Product(**args)
            db.session.add(product)
            db.session.commit()
            return {'message': 'product created successfully'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error creating product', 'error': str(e)}, 500

    def put(self, id=None):
        if id is None:
            return {'message': 'product id is required'}, 400
        try:
            args = product_parser.parse_args()
            product = Product.query.filter_by(id=id).first()
            if product:
                product.title = args['title']
                product.description = args['description']
                product.price = args['price']
                product.rating = args['rating']
                product.stock = args['stock']
                product.brand = args['brand']
                product.category = args['category']
                db.session.commit()
                return {'message': 'product updated successfully'}, 200
            else:
                return {'message': 'product not found'}, 404
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error updating product', 'error': str(e)}, 500

    def delete(self, id=None):
        if id is None:
            return {'message': 'product id is required'}, 400
        try:
            product = Product.query.filter_by(id=id).first()
            if product:
                db.session.delete(product)
                db.session.commit()
                return {'message': 'product deleted successfully'}, 200
            else:
                return {'message': 'product not found'}, 404
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error deleting product', 'error': str(e)}, 500


api.add_resource(ProductList, '/products', '/products/<int:id>')



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)
