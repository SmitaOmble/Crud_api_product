
import unittest
import json
from CRUD_Restful_api import app, db, Product

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_get_all_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to verify the response data if needed

    def test_get_product_by_id(self):
        # Create a test product
        test_product = Product(title='Test Product', price=10.99, rating=4.5, stock=100, brand='Test Brand', category='Test Category')
        db.session.add(test_product)
        db.session.commit()

        # Retrieve the test product by its ID
        response = self.app.get(f'/products/{test_product.id}')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to verify the response data if needed

    def test_create_product(self):
        data = {'title': 'New Product', 'price': 15.99, 'rating': 4.7, 'stock': 50, 'brand': 'New Brand', 'category': 'New Category'}
        response = self.app.post('/products', json=data)
        self.assertEqual(response.status_code, 201)
        # Add more assertions to verify the response data if needed

    def test_update_product(self):
        # Create a test product
        test_product = Product(title='Test Product', price=10.99, rating=4.5, stock=100, brand='Test Brand',
                               category='Test Category')
        db.session.add(test_product)
        db.session.commit()

        # Update the test product
        updated_data = {'title': 'Updated Product', 'price': 12.99, 'rating': 4.8, 'stock': 80,
                        'brand': 'Updated Brand', 'category': 'Updated Category'}
        response = self.app.put(f'/products/{test_product.id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        # Add more assertions to verify the response data if needed

    def test_delete_product(self):
        # Create a test product
        test_product = Product(title='Test Product', price=10.99, rating=4.5, stock=100, brand='Test Brand',
                               category='Test Category')
        db.session.add(test_product)
        db.session.commit()

        # Delete the test product
        response = self.app.delete(f'/products/{test_product.id}')
        self.assertEqual(response.status_code, 200)
        # Verify that the product is deleted by checking for a 404 response on a GET request
        get_response = self.app.get(f'/products/{test_product.id}')
        self.assertEqual(get_response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

