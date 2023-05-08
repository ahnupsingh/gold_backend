from django.urls import path

from app.user import views as user_views

urlpatterns = {
    # User
    path(r'v1/create_account/', user_views.create_account, name='Create Account'),
}
