from flask import Blueprint

from .controllers.teacher_controller import create_teacher, get_teachers, get_teacher, update_teacher, delete_teacher
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user
from app.controllers.menu_controller import create_menu, get_menu, get_menus, update_menu, delete_menu, create_submenu, get_submenu, get_submenus, update_submenu, delete_submenu
from app.controllers.product_controller import create_product ,get_products,get_product,update_product,delete_product
from app.controllers.class_controller import create_class ,get_classes,get_class,update_class,delete_class
from app.controllers.event_controller import create_event,get_events,get_event,update_event,delete_event
#from app.controllers.productDetail_controller import create_productDetail,get_productsDetail,get_productDetail,update_productDetail,delete_productDetail
#from app.controllers.class_controller import create_class ,get_classes,get_class,update_class,delete_class
#from app.controllers.classDetail_controller import create_classDetail,get_classesDetail,get_classDetail,update_classDetail,delete_classDetail
#from app.controllers.event_controller import create_event,get_events,get_event,update_event,delete_event
#from app.controllers.eventContent_controller import create_eventContent,get_eventContents,get_eventContent,update_eventContent,delete_eventContent
#from app.controllers.eventDetail_controller import create_eventDetail,get_eventDetails,get_eventDetail,update_eventDetail,delete_eventDetail
from app.controllers.auth_controller import login, protected

def register_routes(app):
    api = Blueprint('api', __name__)
   
# teacher routes
    api.add_url_rule('/teachers', 'create_teacher', create_teacher, methods=['POST'])
    api.add_url_rule('/teachers', 'get_teachers', get_teachers, methods=['GET'])
    api.add_url_rule('/teachers/<teacher_id>', 'get_teacher', get_teacher, methods=['GET'])
    api.add_url_rule('/teachers/<teacher_id>', 'update_teacher', update_teacher, methods=['PUT'])
    api.add_url_rule('/teachers/<teacher_id>', 'delete_teacher', delete_teacher, methods=['DELETE'])
    
    # user routes
    api.add_url_rule('/users', view_func=create_user, methods=['POST'])
    api.add_url_rule('/users', view_func=get_users, methods=['GET'])
    api.add_url_rule('/users/<user_id>', view_func=get_user, methods=['GET'])
    api.add_url_rule('/users/<user_id>', view_func=update_user, methods=['PUT'])
    api.add_url_rule('/users/<user_id>', view_func=delete_user, methods=['DELETE'])
    
    # menu routes
    api.add_url_rule('/menus', view_func=create_menu, methods=['POST'])
    api.add_url_rule('/menus', view_func=get_menus, methods=['GET'])
    api.add_url_rule('/menus/<menu_id>', view_func=get_menu, methods=['GET'])
    api.add_url_rule('/menus/<menu_id>', view_func=update_menu, methods=['PUT'])
    api.add_url_rule('/menus/<menu_id>', view_func=delete_menu, methods=['DELETE'])
    
    #submenu routes
    api.add_url_rule('/submenus', view_func=create_submenu, methods=['POST'])
    api.add_url_rule('/submenus', view_func=get_submenus, methods=['GET'])
    api.add_url_rule('/submenus/<submenu_id>', view_func=get_submenu, methods=['GET'])
    api.add_url_rule('/submenus/<submenu_id>', view_func=update_submenu, methods=['PUT'])
    api.add_url_rule('/submenus/<submenu_id>', view_func=delete_submenu, methods=['DELETE'])

    #products routes
    
    api.add_url_rule('/products', view_func=create_product, methods=['POST'])
    api.add_url_rule('/products', view_func=get_products, methods=['GET'])
    api.add_url_rule('/products/<product_id>', view_func=get_product, methods=['GET'])
    api.add_url_rule('/products/<product_id>', view_func=update_product, methods=['PUT'])
    api.add_url_rule('/products/<product_id>', view_func=delete_product, methods=['DELETE'])

    # productDetail routes

    # api.add_url_rule('/productDetail', view_func=create_productDetail, methods=['POST'])
    # api.add_url_rule('/productDetail', view_func=get_productsDetail, methods=['GET'])
    # api.add_url_rule('/productDetail/<product_id>', view_func=get_productDetail, methods=['GET'])
    # api.add_url_rule('/productDetail/<product_id>', view_func=update_productDetail, methods=['PUT'])
    # api.add_url_rule('/productDetail/<product_id>', view_func=delete_productDetail, methods=['DELETE'])


    # class routes
    api.add_url_rule ('/classes', view_func= create_class, methods=['POST'])
    api.add_url_rule ('/classes', view_func= get_classes, methods=['GET'])
    api.add_url_rule ('/classes/<class_id>', view_func= get_class, methods=['GET'])
    api.add_url_rule ('/classes/<class_id>', view_func= update_class, methods=['PUT'])
    api.add_url_rule ('/classes/<class_id>', view_func= delete_class, methods=['DELETE'])



# Event
    api.add_url_rule ('/events', view_func= create_event, methods=['POST'])
    api.add_url_rule ('/events', view_func= get_events, methods=['GET'])
    api.add_url_rule ('/events/<eventId>', view_func= get_event, methods=['GET'])
    api.add_url_rule ('/events/<eventId>', view_func= update_event, methods=['PUT'])
    api.add_url_rule ('/events/<eventId>', view_func= delete_event, methods=['DELETE'])





# Authentication routes
    api.add_url_rule('/login', 'login', login, methods=['POST'])
    api.add_url_rule('/protected', 'protected', protected, methods=['GET'])

    app.register_blueprint(api, url_prefix='/api')
