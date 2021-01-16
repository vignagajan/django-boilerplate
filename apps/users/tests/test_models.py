import pytest
from apps.users.models import User

# User creation
@pytest.mark.django_db
def test_user_create():
  user = User.objects.create_user('test@example.com','password',first_name='firstname', last_name='lastname')
  assert User.objects.count() == 1
  assert user.first_name == 'firstname'
  assert user.last_name == 'lastname'
  assert user.email == 'test@example.com'

# Superuser creation
@pytest.mark.django_db
def test_superuser_create():
  superuser = User.objects.create_superuser('test@example.com','password')
  assert User.objects.count() == 1
  assert superuser.email == 'test@example.com'