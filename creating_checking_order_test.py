#Пономарёв Владислав, 8а-когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# Функция на проверку данных о заказе
def test_get_order_by_track():
    order_track = sender_stand_request.get_number_order()
    order_response = sender_stand_request.get_order_by_number(order_track)
    assert order_response.status_code == 200