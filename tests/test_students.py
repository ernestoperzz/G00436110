import pytest

def test_get_student_by_id(client):
    student_id=client.post("/api/students", json = user_payload()).json()["id"]; response = client.get(f"/api/students/{student_id}")
    assert response.status_code == 200

@pytest.mark.parametrize("bad_student_id", ["BAD234", "D123", "stQW4567"])
def test_invalid_student_id_returns_422(client, bad_student_id):
    response = client.post("/api/students", json = user_payload(student_id= bad_student_id))
    assert response.status_code ==422