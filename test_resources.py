import pytest
import requests


def test_get_game():
    response = requests.get("http://localhost:5000/games/1")
    assert response.status_code == 200

def test_get_games():
    response = requests.get("http://localhost:5000/games")
    assert response.status_code == 200

def test_players():
    response = requests.get("http://localhost:5000/games/1")
    assert response.json()['players'] == ['Isgalamido']

def test_create_games():
    response = requests.get("http://localhost:5000/games")
    assert 'game_10' in response.json()

def test_create_kills():
    response = requests.get("http://localhost:5000/games/21")
    assert 'Assasinu Credi' in response.json()['kills']

def test_create_type_of_death():
    response = requests.get("http://localhost:5000/games/21")
    assert 'MOD_RAILGUN' in response.json()['kills_by_means']

def test_world_kills():
    response = requests.get("http://localhost:5000/games/5")
    assert response.json()['world_kills'] == 5

def test_total_kills():
    response = requests.get("http://localhost:5000/games/5")
    assert response.json()['total_kills'] == 14
