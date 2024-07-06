from django.urls import path, include
from django.contrib import admin
from users import views
from users.views import home, users, list_users, routes, promotions, devices
from users.views import( home, users, list_users, routes, promotions, devices,
    add_route, edit_route, delete_route, affectation_routes_users,
    load_devices, assign_user_to_route, assign_client_to_route,
    get_routes, get_route_clients, affectation_clients_routes,
    save_user, get_users, edit_user, user_parameters, search_baskets, assign_promotions,add_basket, define_basket, load_entities,assign_entity)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', home, name='home'),
    path('users/', users, name='users'),
    path('routes/', routes, name='routes'),
    path('routes/add/', add_route, name='add_route'),
    path('routes/edit/<int:route_id>/', edit_route, name='edit_route'),
    path('routes/delete/<int:route_id>/', delete_route, name='delete_route'),
    path('routes/affectation-routes-users/', affectation_routes_users, name='affectation_routes_users'),
    path('routes/affectation-routes-users/', assign_user_to_route, name='assign_user_to_route'),
    path('promotions/search_baskets/', views.search_baskets, name='search_baskets'),
    path('promotions/get_basket/<int:basket_id>/', views.get_basket, name='get_basket'),
    path('routes/get-routes/', views.get_routes, name='get_routes'),
    path('routes/get-route-clients/', views.get_route_clients, name='get_route_clients'),
    path('routes/assign-client-to-route/', views.assign_client_to_route, name='assign_client_to_route'),
    path('routes/affectation-clients-routes/', views.affectation_clients_routes, name='affectation_clients_routes'),
    path('promotions/', promotions, name='promotions'),
    path('promotions/assign_promotions', assign_promotions, name='assign_promotions'),
    path('promotions/load_entities/', views.load_entities, name='load_entities'),
    path('promotions/assign_entity/', views.assign_entity, name='assign_entity'),
    path('promotions/define_basket/', views.define_basket, name='define_basket'),
    path('promotions/add_basket/', views.add_basket, name='add_basket'),

    path('promotions/create/', views.create_promotion, name='create_promotion'),
    path('promotions/get/<int:promotion_id>/', views.get_promotion, name='get_promotion'),
    path('promotions/edit/', views.edit_promotion, name='edit_promotion'),
    path('promotions/delete/', views.delete_promotion, name='delete_promotion'),
    path('promotions/update_checkbox/', views.update_checkbox, name='update_checkbox'),

    path('save-user/', views.save_user, name='save_user'),
    path('get-users/', views.get_users, name='get_users'),


    path('users/edit_user/<str:user_code>/', views.edit_user, name='edit_user'),
    path('user_parameters/<str:user_code>/', views.user_parameters, name='user_parameters'),
    path('devices/', devices, name='devices'),
    path('devices/load/', load_devices, name='load_devices'),
    path('users/<str:user_code>/parameters/', views.user_parameters, name='user_parameters'),
    path('client/<int:client_id>/', views.clients, name='Clients'),
    path('client/', views.clients, name='Clients'),
    path('clients/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    path('client/home_client/', views.home_client, name='home_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),



    path('client/statut_Add/', views.statut_client, name='client_status'),
    path('client_status/<int:client_statut_id>/edit/', views.edit_statut_client, name='edit_statut_client'),
    path('client/home_client_status/', views.home_client_status, name='home_client_status'),


]
