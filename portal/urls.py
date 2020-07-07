from django.urls import path
from . import views as portal_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', portal_view.home, name = 'homepage'),
    path('login/', auth_views.LoginView.as_view(template_name ='portal/login.html'), name = 'login'),
    path('logout/', portal_view.logout_view, name = 'logout'),
    path('access/', portal_view.logged_in, name = 'logged_in'),
    path('index/', portal_view.dashboard, name = 'dashboard'),
    path('reg/', portal_view.profile, name = 'reg'),
    #path('payment/', portal_view.payment, name = 'payment'),
    path('payment/', portal_view.payment, name = 'payment'),
    path('trans/<slug:session>/<slug:term>', portal_view.trans, name = 'trans'),
    path('subjects/', portal_view.subjects, name = 'subjects'),
    path('results/pdf/<slug:session>/<slug:choice>', portal_view.pdf_results, name = 'pdf_results'),
    #path('pdf_payments/<slug:session>/<slug:term>', portal_view.pdf_payments, name = 'pdf_payments'),
    path('pdf_payments/', portal_view.pdf_payments, name = 'pdf_payments'),
    path('pdfredirect/', portal_view.pdf_redirect, name = 'pdfredirect'),
    path('results/', portal_view.results, name = 'results'),
    path('about/', portal_view.about, name = 'about'),
    path('students/<slug:class_name>/', portal_view.all_students, name = 'all_students'),
]
