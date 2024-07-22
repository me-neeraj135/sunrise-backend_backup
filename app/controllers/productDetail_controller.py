from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from

from app.models.product_detail_model  import ProductDetailModel
from app import mongo

productDetail_model = ProductDetailModel(mongo)

def create_productDetail():
    data = request.json
    print('pp',data)
    
    productDetail_data = {
        'productId' :data['productId'],
        'currency' :data['currency'],
        'stock':data['stock'],
        'availability':data['availability'],
          "additionalImages": [
            data['additionalImages'],
            
         ],
        "video": data['video'],
        "specifications": data['specifications'],
        "features":data ['features'],
        "color": data['color'],
        "size": data['size'],
        "rating": data['rating'],
        "shippingCost": data['shipping_Cost'],
        "deliveryTime": data['deliveryTime'],
        "returnPolicy": data['returnPolicy'],
        "vendorId": data['vendorId'],
        "vendorName": data['vendorName'],
        "vendorContact": data['vendorContact']
    }
    product_id = productDetail_model.create(productDetail_data)
    return jsonify({"message": "Product added successfully", "product_id": str(product_id)}), 201

def get_productsDetail():
    products = productDetail_model.find({})
    if not products:
        return jsonify({'message': 'No Products found'}), 404
    
    for product in products:
        product['_id'] = str(product['_id'])
    
    return jsonify(products), 200

def get_productDetail(product_id):
    product = productDetail_model.find_one({'_id': ObjectId(product_id)})
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    product['_id'] = str(product['_id'])
    return jsonify(product), 200

def update_productDetail(product_id):
    data = request.json
    product = productDetail_model.find_one({'_id': ObjectId(product_id)})
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    product_data = {
        'productId' :data['productId'],
        'currency' :data['currency'],
        'stock':data['stock'],
        'availability':data['availability'],
          "additionalImages": [
            data['additionalImages'],
            
         ],
        "video": data['video'],
        "specifications": data['specifications'],
        "features":data ['features'],
        "color": data['color'],
        "size": data['size'],
        "rating": data['rating'],
        "shippingCost": data['shipping_Cost'],
        "deliveryTime": data['deliveryTime'],
        "returnPolicy": data['returnPolicy'],
        "vendorId": data['vendorId'],
        "vendorName": data['vendorName'],
        "vendorContact": data['vendorContact']
    }
    result = productDetail_model.update({'_id': ObjectId(product_id)},product_data)
    
    if result.modified_count == 0:
        return jsonify({'error': 'Product update failed'}), 500
    
    return jsonify({'message': 'Product updated successfully'}), 200

def delete_productDetail(product_id):
    result = productDetail_model.delete({'_id': ObjectId(product_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Product not found or delete failed'}), 404
    
    return jsonify({'message': 'Product deleted successfully'}), 200



