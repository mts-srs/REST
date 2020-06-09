import requests
import time

id2 = {
    'first_name': 'Wiillard',
    'last_name': 'Valek',
    'email': 'wvalek3@vk.com',
    'gender': 'Male',
    'ip_address': '67.76.188.26',
    'issue': {
        'deadline': '01.01.2021',
        'todo': 'Shoot some photos',
        'where': 'imageshack.us'
    }
}

Address = "http://127.0.0.1:5000/"

print("GET User")
time.sleep(0.5)
get = requests.get('{}user/id3'.format(Address))
print(get.text)

print("DELETE User")
time.sleep(0.5)
delete = requests.delete('{}user/id4'.format(Address))
print(delete.text)

print("POST User")
time.sleep(0.5)
post = requests.post(Address + "user/id4", json=id2)
print(post.text)
