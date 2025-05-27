from flask import Flask
from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    """Тестирование главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert 'Информация о проектах' in response.data.decode('utf-8')  # Декодируем байты в строку


def test_add_project(client):
    """Тестирование добавления проекта"""
    response = client.post('/add_project', data={
        'project_name': 'Тестовый проект',
        'performer': 'Исполнитель',
        'producer': 'Продюсер',
        'client_company': 'Клиентская компания',
        'work_date': '2023-10-01'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert 'Тестовый проект' in response.data.decode('utf-8')

def test_calculator_redirect(client):
    """Тестирование редиректа на калькулятор"""
    response = client.get('/calculator')
    assert response.status_code == 302
    assert response.location == "https://www.kontur-extern.ru/info/calculator-sno"