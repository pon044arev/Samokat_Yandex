import data
import configuration
import requests

# Функция для создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Функция для получения номера заказа
def get_number_order():
    order_response = post_new_order(data.order_body)
    return order_response.json()["track"]

# Функция получения заказа по его номеру
def get_order_by_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER + f"?t={track}")