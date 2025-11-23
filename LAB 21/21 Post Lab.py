import requests

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        url = self.base_url + "/posts"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()   # list of posts
        return None

    def create_post(self, title, body, user_id):
        url = self.base_url + "/posts"
        data = {"title": title, "body": body, "userId": user_id}
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return response.json()   # created post
        return None


# Example usage
client = JSONPlaceholderClient()

# Get first 3 posts
posts = client.get_posts()
if posts:
    for p in posts[:3]:
        print("Post:", p["title"])

# Create a new post
new_post = client.create_post("My Post", "Hello from client", 1)
if new_post:
    print("Created ID:", new_post["id"])
