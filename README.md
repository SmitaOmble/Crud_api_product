# Product Management API

This API provides CRUD (Create, Read, Update, Delete) operations for managing products.

## Table of Contents

- [Installation](#installation)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Swagger Documentation](#swagger-documentation)

## Installation

1. Clone the repository:
   ```sh
   git clone  https://github.com/SmitaOmble/Crud_api_product.git
   cd Repository

##Install dependencies:

pip install -r requirements.txt

## Run the application:

 python .\CRUD_Restful_api.py

 
## Endpoints

- `GET /products`: Get all products or a specific product by ID.
- `POST /products`: Create a new product.
- `PUT /products/<id>`: Update an existing product by ID.
- `DELETE /products/<id>`: Delete a product by ID.

### Example Usage

1. Create a new product:
   To create a new product, send a POST request to /products with the following JSON payload:

Example using curl:
curl --location 'http://127.0.0.1:5555/products' \
--header 'Content-Type: application/json' \
--data '{
  "title": "Portable Speaker _4 ",
  "description": "Compact portable speaker with Bluetooth connectivity",
  "price": 790.99,
  "rating": 4.4,
  "stock": 60,
  "brand": "JBL",
  "category": "Electronics"
}
'
3. Update an existing product:
   To update an existing product, send a PUT request to /products/<id> with the product ID and the updated JSON payload 

Example using curl:   
curl --location --request PUT 'http://127.0.0.1:5555/products/1' \
--header 'Content-Type: application/json' \
--data '{
  "title": "Portable Speaker _4 ",
  "description": "Compact portable speaker with Bluetooth connectivity",
  "price": 790.99,
  "rating": 4.4,
  "stock": 60,
  "brand": "JBL",
  "category": "Electronics"
}

4. Delete a product:
   To delete a product, send a DELETE request to /products/<id> with the product ID.
   Example using curl:
curl --location --request DELETE 'http://127.0.0.1:5555/products/1' \
--header 'Content-Type: application/json' \

}
'
5. Get all the product list :
curl --location 'http://127.0.0.1:5555/products/1' \
--data ''


Swagger Documentation
For detailed API documentation and interactive testing, you can access the Swagger UI at http://localhost:5555/swagger.







