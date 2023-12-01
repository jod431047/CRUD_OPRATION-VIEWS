from django.urls import path, include
from .views import TobeList,TobeDetail,TobeCreate, TobeEdit , TobeDelete
from .api import TobeViewset
from rest_framework.routers import DefaultRouter ### 


app_name='tobe'
router = DefaultRouter()
router.register('',TobeViewset)



urlpatterns = [

    path('api/', include(router.urls)),

    path('tobe/', TobeList.as_view()),
    path('tobe/<int:pk>', TobeDetail.as_view()),
    path('list/new',TobeCreate.as_view()),             # create
    path('list/<int:pk>/edit',TobeEdit.as_view()),     # edit
    path('list/<int:pk>/delete',TobeDelete.as_view()), # delet
    ]