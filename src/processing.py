from typing import Union


def filter_by_state(operations_list, state='EXECUTED'):
    """
    Фильтрует список операций по статусу (по умолчанию выбирает 'EXECUTED')

    Параметры:
        operations_list - список словарей с операциями
        state - статус операций для отбора (по умолчанию 'EXECUTED')

    Возвращает:
        Новый список только с операциями указанного статуса
    """

    # Создаем пустой список для результатов
    result = []

    # Перебираем все операции в списке
    for operation in operations_list:
        # Проверяем есть ли в операции ключ 'state'
        if 'state' in operation:
            # Если статус операции совпадает с нужным
            if operation['state'] == state:
                # Добавляем операцию в результат
                result.append(operation)

    # Возвращаем отфильтрованный список
    return result


def sort_by_date(operations_list, reverse=True):
    """
    Сортирует список операций по дате

    Параметры:
        operations_list - список словарей с операциями
        reverse - порядок сортировки (True - новые сначала, False - старые сначала)

    Возвращает:
        Новый список с операциями, отсортированными по дате
    """

    # Создаем копию списка, чтобы не менять оригинал
    sorted_list = operations_list.copy()

    # Функция для получения даты из операции (нужна для сортировки)
    def get_date(operation):
        return operation['date']

    # Сортируем список по дате
    # reverse=True - сортировка по убыванию (новые сначала)
    # reverse=False - сортировка по возрастанию (старые сначала)
    sorted_list.sort(key=get_date, reverse=reverse)

    # Возвращаем отсортированный список
    return sorted_list


