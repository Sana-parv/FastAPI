
from fastapi import status
from routers.todos import get_db
from routers.auth import get_current_user
from models import Todo

from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/todos1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
         'id':1,
        'title' :'learn to code',
        'description':'Need to learn everyday!',
        'priority':5,
        'complete':False,
        'owner_id':1}]


def test_read_one_authenticated(test_todo):
    response = client.get("/todos1/todos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
         'id':1,
        'title' :'learn to code',
        'description':'Need to learn everyday!',
        'priority':5,
        'complete':False,
        'owner_id':1}

def test_read_one_authenticated_not_found(test_todo):
    response = client.get('/todos1/todos/99')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": 'Todo not found'}


def test_create_todo_authenticated(test_todo):
    request_date={
        'title': 'New Todo!',
        'description': 'New Todo description',
        'priority': 5,
        'complete': False
    }
    response = client.post('/todos1/todos/', json=request_date)
    assert response.status_code == 201

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 2).first()
    assert model.title == request_date.get('title')
    assert model.description == request_date.get('description')
    assert model.priority == request_date.get('priority')
    assert model.complete == request_date.get('complete')

def test_update_todo_authenticated(test_todo):
    request_data={
        'title': 'Change the title f the tdo already saved!',
        'description': "Need to learn everyday!",
        'priority': 5,
        'complete': False
    }
    response = client.put('/todos1/todos/1', json=request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 1).first()
    assert model.title == 'Change the title f the tdo already saved!'


def test_update_todo_authenticated_not_found(test_todo):
    request_data={
        'title': 'Change the title f the tdo already saved!',
        'description': "Need to learn everyday!",
        'priority': 5,
        'complete': False
    }
    response = client.put('/todos1/todos/999', json=request_data)
    assert response.status_code == 404
    assert response.json() == {"detail": 'Todo not found'}

def test_delete_todo(test_todo):
    response = client.delete('/todos1/todos/1')
    assert response.status_code == 204
    db = TestingSessionLocal()
    model  = db.query(Todo).filter(Todo.id == 1).first()
    assert model is None

def test_delete_todo_not_found():
    response = client.delete('/todos1/todos/999')
    assert response.status_code == 404
    assert response.json() == {"detail": "not deleted"}
