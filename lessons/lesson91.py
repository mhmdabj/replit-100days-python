def get_dad_joke(requests_module):
    result = requests_module.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
    joke = result.json()
    return joke["joke"]

if __name__ == "__main__":
    class MockResponse:
        def json(self):
            return {"joke": "Why did the chicken cross the road? To get to the other side!", "id": "abc123"}
    class MockRequests:
        @staticmethod
        def get(url, headers=None):
            return MockResponse()
    print(get_dad_joke(MockRequests)) 