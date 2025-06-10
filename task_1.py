import heapq

def min_cost_to_connect_cables(cables):
    """
    Обчислює мінімальні витрати на об'єднання кабелів.

    Args:
        cables (list): Список довжин кабелів.

    Returns:
        int: Мінімальні загальні витрати.
        
    Часова складність: O(n log n), де n - кількість кабелів.
    """
    # Перевірка базового випадку. `len(cables) < 2` є достатньою.
    if len(cables) < 2:
        return 0

    # Перетворюємо список на мінімальну купу "на місці" (in-place).
    # Це ефективно і достатньо для даного завдання.
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість поточного з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий (об'єднаний) кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання:
cable_lengths = [4, 3, 2, 6]
print(f"Довжини кабелів: {cable_lengths}")
# Важливо: функція змінить цей список.
cost = min_cost_to_connect_cables(cable_lengths)
print(f"Мінімальні витрати на з'єднання: {cost}")
print(f"Список кабелів після виконання функції: {cable_lengths}")
