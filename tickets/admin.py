from django.contrib import admin
from .models import Ticket, Response, Comment
from django.contrib.auth.models import User


class ResponseInline(admin.TabularInline):
    model = Response


class CommentInline(admin.TabularInline):
    model = Comment
    max_num = 1


class CommentAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]


class TicketAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ResponseInline]


# Register your models here.
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)