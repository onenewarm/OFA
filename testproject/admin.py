from django.contrib import admin
from .models import User, Account, Subscription, RecommendSub
# Register your models here.


admin.site.register(User)
admin.site.register(Account)
admin.site.register(Subscription)
admin.site.register(RecommendSub)
