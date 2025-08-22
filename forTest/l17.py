import requests

def all_posts():
    req = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    req = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    print(req[0])

all_posts()


def parse():
    body = {
        "userId": 1, "title": "rneoigno3w4gno3wrg5n", "id":"25"
    }
    headers={'Content-Type': 'application/json'}
    resp = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    ).json()
    print(resp)

parse()