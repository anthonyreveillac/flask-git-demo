from app import calculate_age, get_zodiac_sign, days_to_birthday, app, is_birthday_today
from datetime import date
import pytest

def test_calculate_age():
    assert calculate_age("1990-01-01") == date.today().year - 1990

def test_get_zodiac_sign():
    assert get_zodiac_sign("1990-01-01") == "Capricorn"
    assert get_zodiac_sign("1990-07-01") == "Cancer"

def test_days_to_birthday():
    today = date.today()
    next_birthday = date(today.year, 12, 31)
    if next_birthday < today:
        next_birthday = date(today.year + 1, 12, 31)
    expected_days = (next_birthday - today).days
    assert days_to_birthday("2000-12-31") == expected_days
    
def test_is_birthday_today():
    today = date.today()
    assert is_birthday_today(f"{today.year}-{today.month:02d}-{today.day:02d}") == True
    assert is_birthday_today("1990-01-01") == (date.today().month == 1 and date.today().day == 1)
    
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Birthday App" in response.data

def test_birthday_today(client):
    today = date.today()
    response = client.post('/', data={
        'name': 'John Doe',
        'dob': f"{today.year}-{today.month:02d}-{today.day:02d}"
    }, follow_redirects=True)
    assert b"Happy Birthday!" in response.data

def test_birthday_today(client):
    today = date.today()
    response = client.post('/', data={
        'name': 'John Doe',
        'dob': f"{today.year}-{today.month:02d}-{today.day:02d}"
    }, follow_redirects=True)
    assert b"Happy Birthday!" in response.data
