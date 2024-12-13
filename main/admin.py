from django.contrib import admin

# Register your models here.
from . models import UserProfile,MySkill,Certificate,Project,Blog,ContactProfile,Testimonial


admin.site.register(UserProfile)
admin.site.register(MySkill)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(ContactProfile)
admin.site.register(Testimonial)
