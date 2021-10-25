from django.views.generic import RedirectView
from django.urls import include, path

urlpatterns = [
    # Redirect to leaderboard
    path('', RedirectView.as_view(url='leaderboard/highscores/sample_game/')),
    # Leaderboard
    path('leaderboard/', include('django_leaderboard.urls')),
    # auth support for rest framework
    path('restframework/', include('rest_framework.urls', namespace='rest_framework'))
]
