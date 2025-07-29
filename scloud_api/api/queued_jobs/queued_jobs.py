from scloud_api.base import Client, ApiResponse

class QueuedJobs(Client):
    def get_job_status(self, job_id) -> ApiResponse:
        return self._request(f"/api/QueuedJobs/{job_id}", "GET")