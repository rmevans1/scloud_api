class ApiResponse:
    def __init__(self, response):
        self.payload = response['Items'] if 'Items' in response else response
        self.total_results = response['TotalResults'] if 'TotalResults' in response else None