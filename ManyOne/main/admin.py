from django.contrib import admin

# Register your models here.
from .models import BookModel, PublishedModel, DescriptionModel,AuthorModel,GanreModel, ImageModel
admin.site.register(BookModel)
admin.site.register(PublishedModel)
admin.site.register(DescriptionModel)
admin.site.register(AuthorModel)
admin.site.register(GanreModel)
admin.site.register(ImageModel)