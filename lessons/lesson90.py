import json

def get_random_user(requests_module):
    result = requests_module.get("https://randomuser.me/api/")
    user = result.json()
    name = f"{user['results'][0]['name']['first']} {user['results'][0]['name']['last']}"
    image = user['results'][0]['picture']['medium']
    return name, image

if __name__ == "__main__":
    class MockResponse:
        def json(self):
            return {
                "results": [
                    {
                        "name": {"first": "John", "last": "Doe"},
                        "picture": {"medium": "http://example.com/image.jpg"}
                    }
                ]
            }
    class MockRequests:
        @staticmethod
        def get(url):
            return MockResponse()
    name, image = get_random_user(MockRequests)
    print(name)
    print(image) 