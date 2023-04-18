from rest_framework.routers import DefaultRouter
from .views import ParentViewset, TeacherViewset, StudentViewset

router = DefaultRouter()

router.register("parents", ParentViewset)
router.register("teachers", TeacherViewset)
router.register("students", StudentViewset)


urlpatterns = router.urls