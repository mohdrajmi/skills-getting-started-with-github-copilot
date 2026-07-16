from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_from_activity():
    activity_name = "Chess Club"
    email = "newstudent@example.com"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert unregister_response.status_code == 200

    activity_response = client.get("/activities")
    activities = activity_response.json()
    assert email not in activities[activity_name]["participants"]
