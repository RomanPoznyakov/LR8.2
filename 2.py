
def check_query(query):
    elements = query.split()  # Разделяем запрос на отдельные слова
    if elements[0] == 'Анфиса,':  # Проверяем, начинается ли запрос с "Анфиса,"
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'

# Заранее заданные запросы
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Печать результата для каждого запроса
for q in queries:
    result = check_query(q)
    print(q, '-', result)
