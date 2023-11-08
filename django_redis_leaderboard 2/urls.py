"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import RedirectView, TemplateView
from django.urls import include, path


urlpatterns = [
    # Redirect to leaderboard
    path('', RedirectView.as_view(url='leaderboard/highscores/sample_game/')),
    # Leaderboard
    path('leaderboard/', include('leaderboard_app.urls')),
    # auth support for rest framework
    path('restframework/', include('rest_framework.urls', namespace='rest_framework')),
    # path('admin/', admin.site.urls),
    path('hello-webpack/', TemplateView.as_view(template_name='leaderboard_app/hello_webpack.html'))
]
