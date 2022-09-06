from locale import currency
import site
from django.contrib import admin
from .models import Customer,Wallet,Transaction,Account,Card,Receipt,Reward,Loan,Currency
from .models import Thirdparty
from .models import Notification

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    search_fields=("first_name","last_name")

admin.site.register(Customer,CustomerAdmin)    


class WalletAdmin(admin.ModelAdmin):
    list_display=("balance","date","is_active",)
    search_fields=("balance","is_active")

admin.site.register(Wallet,WalletAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display=("wallet","name","account_type",)
    search_fields=("balance","is_active")
admin.site.register(Account,AccountAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=("signature","account","date_issued",)
    search_fields=("account","signature")
admin.site.register(Card,CardAdmin)    


class ThirdParytAdmin(admin.ModelAdmin):
    list_display=("email", "phone_number","transaction_cost",)
    search_fields=("balance","is_active")
admin.site.register(Thirdparty,ThirdParytAdmin) 

class NotificationAdmin(admin.ModelAdmin):
    list_display=("message","data_created","is_active",)
    search_fields=("balance","is_active")
admin.site.register(Notification,NotificationAdmin) 

class RewardAdmin(admin.ModelAdmin):
    list_display=("name","date")
    search_fields=("name","date")
admin.site.register(Reward,RewardAdmin)  

class LoanAdmin(admin.ModelAdmin):
    list_display=("balance","date_time","amount",)
    search_fields=("balance","amount")
admin.site.register(Loan,LoanAdmin) 
 

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt","transaction","file","date",)
    search_fields=("receipt","file")
admin.site.register(Receipt,ReceiptAdmin) 

class TransactionAdmin(admin.ModelAdmin):
    list_display=("amount","thirdparty","status","account_origin","destination","receipt",)
    search_fields=("balance","is_active")
admin.site.register(Transaction,TransactionAdmin)  

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("symbol","name","country",)
    search_fields=("symbol","name")
admin.site.register(Currency,CurrencyAdmin) 





