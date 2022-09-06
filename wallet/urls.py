# from nturl2path import url2pathname

from django .urls import path
from .views import register_customer
from .views import register_account
from .views import register_card
from .views import register_currency
from .views import register_transaction
from .views import register_thirdparty
from .views import register_notification
from .views import register_receipt
from .views import register_reward





urlpatterns = [path("register/", register_customer, name="customer"),]

urlpatterns = [path("register/", register_account, name="account"),]

urlpatterns = [path("register/", register_card, name="card"),]

urlpatterns = [path("register/",register_currency,name="currency"),]

urlpatterns = [path("register/",register_transaction,name="transaction"),]

urlpatterns = [path("register/", register_thirdparty, name="thirdparty"),]

urlpatterns = [path("register/", register_notification, name="nofification"),]

urlpatterns = [path("register/", register_receipt, name="receipt"),]

urlpatterns = [path("register/", register_reward, name="receipt"),]















