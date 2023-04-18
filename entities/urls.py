from rest_framework.routers import DefaultRouter
from .views import DivisionViewset, SectionViewset

router = DefaultRouter()

router.register("divisions", DivisionViewset)
router.register("sections", SectionViewset)


urlpatterns =  router.urls