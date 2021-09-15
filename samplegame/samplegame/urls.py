from django.http import HttpResponseRedirect
from django.conf.urls import include, url

urlpatterns = [
    # Redirect to leaderboard
    url(r'^$', lambda r : HttpResponseRedirect('leaderboard/highscores/sample_game/')),

    # Leaderboard
    url(r'^leaderboard/', include('django_leaderboard.urls')),

    # auth support for rest framework
    url(r'^restframework', include('rest_framework.urls', namespace='rest_framework'))
]
