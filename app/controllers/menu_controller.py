from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.menu_model import MenuModel
from app.models.submenu_model import SubmenuModel
from app import mongo

menu_model = MenuModel(mongo)
submenu_model = SubmenuModel(mongo)

# Swagger documentation annotations can be added as needed

# Menu CRUD Operations

def create_menu():
    data = request.json
    menu_data = {
        "title": data["title"],
        "menuClass": data["menuClass"],
        "isActive": data.get("isActive", 1),
        "userId": data["userId"],
        "orderBy": data["orderBy"]
    }
    menu_id = menu_model.create(menu_data)
    return jsonify({"message": "Menu created successfully", "menu_id": str(menu_id)}), 201

def get_menus():
    menus = menu_model.find({})
    if not menus:
        return jsonify({'message': 'No menus found'}), 404
    
    for menu in menus:
        menu['_id'] = str(menu['_id'])
    
    return jsonify(menus), 200

def get_menu(menu_id):
    menu = menu_model.find_one({'_id': ObjectId(menu_id)})
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    menu['_id'] = str(menu['_id'])
    return jsonify(menu), 200

def update_menu(menu_id):
    data = request.json
    menu = menu_model.find_one({'_id': ObjectId(menu_id)})
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    menu_data = {
        "title": data["title"],
        "menuClass": data["menuClass"],
        "isActive": data.get("isActive", 1),
        "userId": data["userId"],
        "orderBy": data["orderBy"]
    }
    result = menu_model.update({'_id': ObjectId(menu_id)}, menu_data)
    
    if result.modified_count == 0:
        return jsonify({'error': 'Menu update failed'}), 500
    
    return jsonify({'message': 'Menu updated successfully'}), 200

def delete_menu(menu_id):
    result = menu_model.delete({'_id': ObjectId(menu_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Menu not found or delete failed'}), 404
    
    return jsonify({'message': 'Menu deleted successfully'}), 200

# Submenu CRUD Operations

def create_submenu():
    data = request.json
    submenu_data = {
        "menuId": data["menuId"],
        "title": data["title"],
        "route": data["route"],
        "subMenuClass": data["subMenuClass"],
        "isActive": data.get("isActive", 1),
        "userId": data["userId"],
        "subSubMenu": data.get("subSubMenu", [])
    }
    submenu_id = submenu_model.create(submenu_data)
    return jsonify({"message": "Submenu created successfully", "submenu_id": str(submenu_id)}), 201

def get_submenus():
    submenus = list(submenu_model.find({}))
    if not submenus:
        return jsonify({'message': 'No submenus found'}), 404
    
    for submenu in submenus:
        submenu['_id'] = str(submenu['_id'])
    
    return jsonify(submenus), 200

def get_submenu(submenu_id):
    submenu = submenu_model.find_one({'_id': ObjectId(submenu_id)})
    if not submenu:
        return jsonify({'error': 'Submenu not found'}), 404

    submenu['_id'] = str(submenu['_id'])
    return jsonify(submenu), 200

def update_submenu(submenu_id):
    data = request.json
    submenu = submenu_model.find_one({'_id': ObjectId(submenu_id)})
    if not submenu:
        return jsonify({'error': 'Submenu not found'}), 404

    submenu_data = {
        "menuId": data["menuId"],
        "title": data["title"],
        "route": data["route"],
        "subMenuClass": data["subMenuClass"],
        "isActive": data.get("isActive", 1),
        "userId": data["userId"],
        "subSubMenu": data.get("subSubMenu", [])
    }
    result = submenu_model.update({'_id': ObjectId(submenu_id)}, {"$set": submenu_data})
    
    if result.modified_count == 0:
        return jsonify({'error': 'Submenu update failed'}), 500
    
    return jsonify({'message': 'Submenu updated successfully'}), 200

def delete_submenu(submenu_id):
    result = submenu_model.delete({'_id': ObjectId(submenu_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Submenu not found or delete failed'}), 404
    
    return jsonify({'message': 'Submenu deleted successfully'}), 200
