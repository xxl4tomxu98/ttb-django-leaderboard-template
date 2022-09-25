from django.urls import include, path, re_path
from django.views.generic import RedirectView
from .views import ScoresView, ScoresAroundMeView, highscores

urlpatterns = [
    # Api urls
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),    
    path('api/<str:game>/user/<int:user_id>/', ScoresAroundMeView.as_view(), name='leaderboard_around_me_api'),
    path('api/<str:game>/', ScoresView.as_view(), name='leaderboard_api'),
    path('api/<str:game>/<int:page>/', ScoresView.as_view(), name='leaderboard_api_with_page'),

    # the leaderboard for the high scores
    path('highscores/<str:game>/', highscores, name="leaderboard_high_scores"),
    path('highscores/<str:game>/<int:page>/', highscores, name="leaderboard_high_scores_with_page"),
]
