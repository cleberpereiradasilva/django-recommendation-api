from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagViewSet
router = DefaultRouter(trailing_slash=False)

# TODO: Register endpoint's URLs here

router.register('post', PostViewSet)
router.register('tag', TagViewSet)



urlpatterns = router.urls
