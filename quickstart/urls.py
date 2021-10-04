from django.urls import path
from quickstart import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('api-root/', views.api_root),
    path('snippets/', views.SnippetListGeneric.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetailGeneric.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)