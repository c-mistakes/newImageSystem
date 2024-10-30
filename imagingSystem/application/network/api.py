import requests

class ApiService:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def update_resolution(self, path, width, height):
        url = f"{self.base_url}/image/process/resolution/"
        data = {
            "path": path,
            "width": width,
            "height": height
        }
        response = requests.put(url, json=data, headers=self.headers)
        return response.status_code, response.json()
