import requests


class YGProject:

    def __init__(self, url, api_key):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

    def create_project(self, name):
        project = {
            'title': name,
            'users': {
                "0aa8fe91-0b40-4403-890b-045a4040b172": "admin"
            }
        }
        resp = requests.post(f'{self.url}/projects', headers=self.headers,
                             json=project)
        return resp

    def change_name_project(self, id, name, deleted=False):
        change = {
            "deleted": deleted,
            "title": name,
            "users": {
                "0aa8fe91-0b40-4403-890b-045a4040b172": "admin"
            }
        }
        resp = requests.put(f'{self.url}/projects/{id}', headers=self.headers,
                            json=change)
        return resp

    def delete_project(self, id, deleted=True):
        change = {
            "deleted": deleted,
            "users": {
                "0aa8fe91-0b40-4403-890b-045a4040b172": "admin"
            }
        }
        resp = requests.put(f'{self.url}/projects/{id}', headers=self.headers,
                            json=change)
        return resp

    def get_project_with_id(self, id):
        resp = requests.get(f'{self.url}/projects/{id}',
                            headers=self.headers)
        return resp
