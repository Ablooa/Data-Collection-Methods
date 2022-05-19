import requests
import json

User = input('Имя пользователя для вывода списка репозиториев: ')
url = f"https://api.github.com/users/{User}/repos"
data = {"type": "all", "sort": "full_name", "direction": "asc"}

output = requests.get(url, data = json.dumps(data))
output = json.loads(output.text)
print(f'Открытые репозитории пользователя {User}: ')
for i in output:
    print(i['name'])
