from django.urls import path, include
from quickstart import views 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destory'
# })

# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })

# groups = views.GroupViewSet.as_view({
#     'get': 'list'
# })

# group_detail = views.GroupViewSet.as_view({
#     'get': 'retrieve'
# })

#Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet),
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

    # path('', views.api_root),
    # path('snippets/', snippet_list, name='snippet-list'),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),
    # path('groups/', groups, name='groups'),
    # path('groups/<int:pk>/', group_detail, name='group-detail')
]

# urlpatterns = format_suffix_patterns(urlpatterns)