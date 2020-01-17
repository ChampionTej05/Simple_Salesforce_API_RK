from rest_framework import routers
from webapp.views import SalesforceViewSet,UserViewSet

router=routers.SimpleRouter()
print("In routers ")
router.register(r'',SalesforceViewSet)
# router.register(r'',UserViewSet,basename='user')
