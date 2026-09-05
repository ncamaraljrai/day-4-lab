from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_f01_create_note() -> None:
    r = client.post("/notes", json={"text": "alpha"})
    assert r.status_code == 201
    assert r.json() == {"id": 1, "text": "alpha"}


def test_f02_read_note() -> None:
    created = client.post("/notes", json={"text": "alpha"}).json()
    r = client.get(f"/notes/{created['id']}")
    assert r.status_code == 200
    assert r.json() == created


def test_f03_list_notes() -> None:
    client.post("/notes", json={"text": "alpha"})
    client.post("/notes", json={"text": "beta"})
    r = client.get("/notes")
    assert r.status_code == 200
    assert r.json() == [{"id": 1, "text": "alpha"}, {"id": 2, "text": "beta"}]


def test_f04_update_note() -> None:
    created = client.post("/notes", json={"text": "alpha"}).json()
    r = client.patch(f"/notes/{created['id']}", json={"text": "updated"})
    assert r.status_code == 200
    assert r.json() == {"id": 1, "text": "updated"}


def test_f05_delete_note() -> None:
    created = client.post("/notes", json={"text": "alpha"}).json()
    r = client.delete(f"/notes/{created['id']}")
    assert r.status_code == 204
    assert client.get(f"/notes/{created['id']}").status_code == 404
