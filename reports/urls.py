from rest_framework.routers import DefaultRouter
from .views import ReportViewset
router = DefaultRouter()

router.register('reports', ReportViewset)

urlpatterns = router.urls