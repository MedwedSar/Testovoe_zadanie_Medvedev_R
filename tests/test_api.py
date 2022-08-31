import requests


def test_api_req():
    res = requests.get('https://reqres.in/api/users/2')
    if res.status_code == 200:
        assert res.json().get('data').get('first_name') == 'Janet', 'Incorrect first name'
