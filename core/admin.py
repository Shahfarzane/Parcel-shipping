from django.contrib import admin
from . import models

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['stripe_payment_intent_id', 'customer', 'courier','job', 'amount', 'status','create_at','courier_paypal_email' ]
    list_filter = ['status',]

    def customer(self,obj):
        return obj.job.customer

    def courier(self, obj):
        return obj.job.courier
    def courier_paypal_email(sefl, obj):
        return obj.job.courier.paypal_email if obj.job.courier else None        


# Register your models here.

admin.site.register(models.Customer)
admin.site.register(models.Courier)
admin.site.register(models.Category)
admin.site.register(models.Job)
admin.site.register(models.Transaction,TransactionAdmin)
