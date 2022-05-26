from django.urls import path

#linijka do "zapomnienie hasła"
from django.contrib.auth import views as auth_views

from . import views

from django.contrib import admin

app_name = 'predict'

# gdyby nie dziala predykcja dla iris to z poprzedniego backupu
# podmienic tylko pierwsze linijki w urlpatterns
# i w base.html -> href="/prediction_page" -> href="/"
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    path('prediction_page', views.predict, name='prediction_page'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('iris_results/', views.iris_view_results, name='iris_results'),
    path('iris_import/', views.iris_import_data, name="iris_import"),
    path('iris_export/', views.iris_export_data, name="iris_export"),
    path('iris_imported/', views.iris_imported, name="iris_imported"),
    path('iris_train_model/', views.iris_train_model, name="iris_train_model"),

    path('udb/', views.udb, name ="udb"),
    path('udbchoice/', views.udbchoice, name="udbchoice"),
    path('udbdf/', views.udbdf, name="udbdf"),
    path('train_model/', views.train_model, name="train_model"),
    path('import_data/', views.import_data, name="import_data"),

    path('testcss/', views.testcss, name="testcss"),
    
    path('register/', views.register, name='registration'),
    path('login/', views.login1, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
    path('panel/', views.panel, name= 'panel'),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
     name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
     name="password_reset_complete"),



]