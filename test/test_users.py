from urllib import response

from utils import *
from routers.users import get_current_user,get_db

app.dependency_overrides[get_current_user] = override_get_current_user
app.dependency_overrides[get_db] = override_get_db

def test_return_user(test_user):
    response = client.get("/Users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == "codingwithsanatest"
    assert response.json()['first_name'] == "sana"
    assert response.json()['last_name'] == "parvin"
    assert response.json()['email'] == 'codingwithsana@gmail.com'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == "(111)-111-1111"

def test_change_password_success(test_user):
    response = client.put("/Users/password",json={"password":"testpassword",
                                                        "new_password":"newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put("/Users/password", json={"password": "wrong_password",
                                                         "new_password": "newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail":"Current password is incorrect"}

def test_change_phone_number_success(test_user):
    response = client.put('/Users/phone_number/22222222222')
    assert response.status_code == status.HTTP_204_NO_CONTENT