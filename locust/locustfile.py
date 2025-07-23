from locust import HttpUser, task, between, constant_throughput

class StudentAppUser(HttpUser):
    wait_time = constant_throughput(1)
    @task
    def get_students(self):
        self.client.get("/students/")


