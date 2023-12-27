from tags.views import (
    CreateTagView, 
    TagDetailViewV1, 
    TagDetailViewV2,
    DeleteTagView1,
    DeleteTagView2,
    TagListView1,
    TagListView2,
)
from django.urls import path

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create-tag'),
    path('tag-detail/v1/<str:slug>', TagDetailViewV1.as_view(), name='tag-detail-v1'),
    path('tag-detail/v2/<str:slug>', TagDetailViewV2.as_view(), name='tag-detail-v2'),
    path('tag-delete/v1/<str:slug>', DeleteTagView1.as_view(), name='delete-tag-v1'),
    path('tag-delete/v2/<str:slug>', DeleteTagView2.as_view(), name='delete-tag-v2'),
    path('tag-list/v1', TagListView1.as_view(), name='tag-list-v1'),
    path('tag-list/v2', TagListView2.as_view(), name='tag-list-v2'),
]