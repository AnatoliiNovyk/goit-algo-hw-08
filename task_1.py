import heapq

def min_cost_to_connect_cables(cables):
    """
    Обчислює мінімальні витрати на об'єднання кабелів.

    Args:
        cables (list): Список довжин кабелів.

    Returns:
        int: Мінімальні загальні витрати.
    """
    if not cables or len(cables) < 2:
        return 0

    # Перетворюємо список на мінімальну купу
    heapq.heapify(cables) # Часова складність O(n) 

    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables) # Часова складність O(log n) 
        second = heapq.heappop(cables) # Часова складність O(log n)

        # Вартість поточного з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий (об'єднаний) кабель назад у купу
        heapq.heappush(cables, cost) # Часова складність O(log n)

    return total_cost

# Приклад використання:
cable_lengths = [4, 3, 2, 6]
print(f"Довжини кабелів: {cable_lengths}")
print(f"Мінімальні витрати на з'єднання: {min_cost_to_connect_cables(cable_lengths)}")

cable_lengths_2 = [1, 1, 2, 3]
print(f"Довжини кабелів: {cable_lengths_2}")
print(f"Мінімальні витрати на з'єднання: {min_cost_to_connect_cables(cable_lengths_2)}")
