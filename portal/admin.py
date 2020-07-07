from django.contrib import admin
from .models import Customuser, Subjectz, Subject_2, Subject_3, Course, Payment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

admin.site.register(Customuser)
#admin.site.register(Subjectz)
admin.site.register(Course)
admin.site.site_header = "Student Portal Admin"


# adding actions to the admin panel
def to_female(modeladmin, request, queryset):
    queryset.update(gender = 'Female')
to_female.short_description = 'Change Gender of selected student(s) to Female'

def to_male(modeladmin, request, queryset):
    queryset.update(gender = 'Male')
to_male.short_description = 'Change Gender of selected student(s) to Male'


class CustomAdmin(BaseUserAdmin):
    list_display = ('username','email','last_name', 'first_name', 'middle_name', 'current_class')
    list_filter = ('current_class','gender','religion','is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('current_class','email', 'last_name', 'first_name', 'middle_name', 'gender', 'phonenumber', 'date_of_birth', 'religion', 'nok1_name',
                  'nok1_phone', 'nok1_relationship', 'admission_no', 'state_of_origin',
                  'lga', 'resident_type', 'house_address', 'prev_school', 'passport','submitted')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'current_class','last_name', 'first_name', 'middle_name', 'password1', 'password2')}
         ),
    )
    actions = [to_female, to_male]

admin.site.unregister(Customuser)
admin.site.unregister(Group)
admin.site.register(Customuser, CustomAdmin)


def session_2019(modeladmin, request, queryset):
    queryset.update(session = '2019/2020')
session_2019.short_description = 'Change session to 2019/2020'

def session_2020(modeladmin, request, queryset):
    queryset.update(session = '2020/2021')
session_2020.short_description = 'Change session to 2020/2021'

@admin.register(Subjectz)
class SubjectzAdmin(admin.ModelAdmin):
    list_display = ('student','title', 'term')
    list_filter = ('student','title', 'term', 'session')
    ordering = ('student',)
    search_fields = ('title', 'student')
    actions = [session_2019, session_2020]

@admin.register(Subject_2)
class SubjectAdmin2(admin.ModelAdmin):
    list_display = ('student','title', 'term')
    list_filter = ('student', 'title', 'term', 'session')
    ordering = ('student',)
    search_fields = ('title', 'student')
    actions = [session_2019, session_2020]

@admin.register(Subject_3)
class SubjectAdmin3(admin.ModelAdmin):
    list_display = ('student','title', 'term')
    list_filter = ('student', 'title', 'term', 'session')
    ordering = ('student',)
    search_fields = ('title', 'student')
    actions = [session_2019, session_2020]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student','term','session', 'amount', 'reference', 'paid')
    list_filter = ('student', 'term', 'session', 'paid')
    ordering = ('student',)
    search_fields = ('student', 'reference')
    readonly_fields = ['student', 'term', 'session', 'amount', 'reference', 'paid']
