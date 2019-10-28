from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'groups', views.GroupListView, basename='group')
router.register(r'users', views.UserListView, basename='user')
urlpatterns = router.urls
