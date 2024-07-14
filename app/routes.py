from flask import Blueprint
from .controllers.teacher_controller import create_teacher, get_teachers, get_teacher, update_teacher, delete_teacher
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user
from app.controllers.menu_controller import create_menu, get_menu, get_menus, update_menu, delete_menu, create_submenu, get_submenu, get_submenus, update_submenu, delete_submenu

def register_routes(app):
    api = Blueprint('api', __name__)

    api.add_url_rule('/teachers', 'create_teacher', create_teacher, methods=['POST'])
    api.add_url_rule('/teachers', 'get_teachers', get_teachers, methods=['GET'])
    api.add_url_rule('/teachers/<teacher_id>', 'get_teacher', get_teacher, methods=['GET'])
    api.add_url_rule('/teachers/<teacher_id>', 'update_teacher', update_teacher, methods=['PUT'])
    api.add_url_rule('/teachers/<teacher_id>', 'delete_teacher', delete_teacher, methods=['DELETE'])
    
    api.add_url_rule('/users', view_func=create_user, methods=['POST'])
    api.add_url_rule('/users', view_func=get_users, methods=['GET'])
    api.add_url_rule('/users/<user_id>', view_func=get_user, methods=['GET'])
    api.add_url_rule('/users/<user_id>', view_func=update_user, methods=['PUT'])
    api.add_url_rule('/users/<user_id>', view_func=delete_user, methods=['DELETE'])
    
    api.add_url_rule('/menus', view_func=create_menu, methods=['POST'])
    api.add_url_rule('/menus', view_func=get_menus, methods=['GET'])
    api.add_url_rule('/menus/<menu_id>', view_func=get_menu, methods=['GET'])
    api.add_url_rule('/menus/<menu_id>', view_func=update_menu, methods=['PUT'])
    api.add_url_rule('/menus/<menu_id>', view_func=delete_menu, methods=['DELETE'])
    
    api.add_url_rule('/submenus', view_func=create_submenu, methods=['POST'])
    api.add_url_rule('/submenus', view_func=get_submenus, methods=['GET'])
    api.add_url_rule('/submenus/<submenu_id>', view_func=get_submenu, methods=['GET'])
    api.add_url_rule('/submenus/<submenu_id>', view_func=update_submenu, methods=['PUT'])
    api.add_url_rule('/submenus/<submenu_id>', view_func=delete_submenu, methods=['DELETE'])

    app.register_blueprint(api, url_prefix='/api')
