from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_activity(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        team = Team.objects.create(name='Test Team 2')
        activity = Activity.objects.create(user=user, team=team, type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team 3')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')
