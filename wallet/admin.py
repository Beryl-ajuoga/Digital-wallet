from locale import currency
from django.contrib import admin
from .models import Customer,Wallet,Transaction,Account,Card,Receipt,Reward,Loan,Currency
from .models import Thirdparty
from .models import Notification

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email")
    search_fields=("first_name","last_name")

admin.site.register(Customer,CustomerAdmin)   
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Reward)
admin.site.register(Loan)
admin.site.register(Currency)