from django.contrib import admin

from .models import Publication,Article,Reporter,ReporterArticle,Place,Restaurant

admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(ReporterArticle)
admin.site.register(Place)
admin.site.register(Restaurant)


