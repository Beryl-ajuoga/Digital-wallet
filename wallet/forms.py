from django import forms
from .models import Customer, Notification, Receipt, Reward
from .models import Account
from .models import Currency
from .models import Card
from .models import Loan
from .models import Transaction
from .models import Thirdparty
from .models import Notification
from .models import Receipt
from .models import Reward






class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields= "__all__"

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields= "__all__"

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields= "__all__"

class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model=Currency
        fields= "__all__"  

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields= "__all__"

class ThirdpartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=Thirdparty
        fields= "__all__"


class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields= "__all__"


class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model=Receipt

        fields= "__all__"


class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Reward

        fields= "__all__"



  






    