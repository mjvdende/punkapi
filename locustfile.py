from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def get_beers(self):
        self.client.get("/beers", params={"per_page": 80, "page": 1})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://localhost:5001/v3"  # Set the base URL here