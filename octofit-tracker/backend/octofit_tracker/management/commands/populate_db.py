from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
from djongo import models

from octofit_tracker import settings as octo_settings

from django.db import connection

# Define models inline for demonstration (in real app, use models.py)
from django.db import models as dj_models

class Team(dj_models.Model):
    name = dj_models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(dj_models.Model):
    user = dj_models.CharField(max_length=100)
    team = dj_models.CharField(max_length=100)
    type = dj_models.CharField(max_length=100)
    duration = dj_models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(dj_models.Model):
    team = dj_models.CharField(max_length=100)
    points = dj_models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(dj_models.Model):
    name = dj_models.CharField(max_length=100)
    description = dj_models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password')

        # Create Activities
        Activity.objects.create(user='ironman', team='Marvel', type='Running', duration=30)
        Activity.objects.create(user='spiderman', team='Marvel', type='Cycling', duration=45)
        Activity.objects.create(user='batman', team='DC', type='Swimming', duration=60)
        Activity.objects.create(user='wonderwoman', team='DC', type='Yoga', duration=50)

        # Create Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)

        # Create Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        Workout.objects.create(name='Agility Training', description='Agility and speed drills')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
