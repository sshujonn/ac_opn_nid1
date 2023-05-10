from django.contrib import admin

# Register your models here.
from ac_openning.models import Account, Customer, SourceOfIncome, Occupation, AccGoal, AccType

admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(SourceOfIncome)
admin.site.register(Occupation)
admin.site.register(AccType)
admin.site.register(AccGoal)