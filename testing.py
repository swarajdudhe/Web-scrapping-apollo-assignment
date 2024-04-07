import pytest
from starlette.testclient import TestClient
from my_fastapi import app

@pytest.fixture
def test_client():
    return TestClient(app)

# def test_start_scraping(test_client):
#     response = test_client.post("/scrape")
#     assert response.status_code == 200
#     assert "job_id" in response.json()

# def test_get_scrape_results_pending(test_client):
#     response = test_client.get("/scrape_results")
#     assert response.status_code == 200
#     assert response.json()["status"] == "pending"

# Assuming you have a valid job_id for completed task
# def test_get_scrape_results_success(test_client):
#     job_id = 123
#     response = test_client.get(f"/scrape_results/{job_id}")
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"
#     assert "scraped_results" in response.json()

# def test_get_scrape_results_failure(test_client):
#     job_id = "your_invalid_job_id"
#     response = test_client.get(f"/scrape_results/{job_id}")
#     assert response.status_code == 200
#     assert response.json()["status"] == "error"
#     assert "message" in response.json()

