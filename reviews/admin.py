from django.contrib import admin

from .models import Gun, GunReview
# Register your models here.

class GunReviewAdmin(admin.ModelAdmin):
	model = GunReview
	list_display = ('gun', 'rating', 'user_name', 'comment', 'pub_date')
	list_filter = ['pub_date', 'user_name']
	search_fields = ['comment', 'gun']

admin.site.register(Gun)
admin.site.register(GunReview, GunReviewAdmin)