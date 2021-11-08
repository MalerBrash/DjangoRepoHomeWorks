import requests

# примеры API-запросов

# URL = https://localhost:8000/api/v1/advertisements/

# получение объявлений
URL = 'http://localhost:8000/api/v1/advertisements/'


###
#
# # создание объявления
# POST {{baseUrl}}/advertisements/
# Content-Type: application/json
# Authorization: Token 902ef055a9ac93f18327f1f9c45ab059f1a62c7d
#
# {
#   "title": "Шкаф IKEA",
#   "description": "Срочно"
# }
#
# ###
#
# # попытка поменять объявление
# PATCH {{baseUrl}}/advertisements/1/
# Content-Type: application/json
# Authorization: Token 902ef055a9ac93f18327f1f9c45ab059f1a62c7d
#
# {
#   "status": "CLOSED"
# }
#
# ###
#
# # фильтрация по создателю
# GET {{baseUrl}}/advertisements/?creator=3
# Content-Type: application/json
#
# ###
#
# # фильтрация по дате
# GET {{baseUrl}}/advertisements/?created_at_before=2020-10-01
# Content-Type: application/json
#
# ##################################
#





##############3


# URL = 'http://localhost:8000/api/v1/advertisements/?creator=2'
# URL = 'http://localhost:8000/api/v1/advertisements/?created_at_before=2021-11-08'
# HEADERS = {
#   'authorization': 'Token b070ea45956fd7cd885a1075bf6c98c5dbd4d949',
# }
#
# if __name__ == '__main__':
#   # resp = requests.post(URL, headers=HEADERS,
#   #                      json={
#   #                        'title': 'Вован2',
#   #                        'description': 'test Вован 2',
#   #                        'status': 'OPEN',
#   #                      })
#
#   # resp = requests.delete('http://127.0.0.1:8000/api/v1/advertisements/7', headers=HEADERS)
#
#   # resp = requests.patch('http://127.0.0.1:8000/api/v1/advertisements/21/', headers=HEADERS,
#   #                      json={
#   #                        'status': 'CLOSED',
#   #                      })
#   # print(resp.status_code, resp.json())
#   resp = requests.get(URL)
#   print(len(resp.json()), resp.json())

