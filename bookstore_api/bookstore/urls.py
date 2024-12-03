from rest_framework.routers import DefaultRouter
from .views import BookViewset, ReviewViewset, UserProfileViewset

router = DefaultRouter()
router.register('books', BookViewset)
router.register('reviews', ReviewViewset)
router.register('profiles', UserProfileViewset)

urlpatterns = router.urls
