import unittest
import requests

class TestPostApi(unittest.TestCase):
    def setUp(self):
        body = {
            "title":"testwords",
            "body":"body body",
            "userId":1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.post_id = response.json()['id']
        print(f'Post created:{self.post_id}')
    
    def test_get_one_post(self):
        post_id = self.new_post()
        response = requests.get(
            f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)
    
    
    
    
    def test_geat_all_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)
        
    def test_add_post(self):
        body = {
            "title":"testwords",
            "body":"body body",
            "userId":1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)

        def tearDown(post_id):
            requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
            print(f'Post created:{self.post_id}')