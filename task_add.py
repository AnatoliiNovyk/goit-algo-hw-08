import heapq

def merge_k_lists(lists):
    """
    Об'єднує k відсортованих списків в один відсортований список.

    Args:
        lists (list of lists): Список відсортованих списків.

    Returns:
        list: Один об'єднаний відсортований список.
    """
    min_heap = []
    
    # Додаємо перший елемент з кожного списку до купи
    for i, lst in enumerate(lists):
        if lst:
            # (значення, індекс_списку, індекс_елемента)
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list = []

    while min_heap:
        # Витягуємо найменший елемент з усіх списків
        value, list_idx, element_idx = heapq.heappop(min_heap)
        
        merged_list.append(value)

        # Якщо в цьому списку є ще елементи, додаємо наступний до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_element_idx = element_idx + 1
            next_value = lists[list_idx][next_element_idx]
            heapq.heappush(min_heap, (next_value, list_idx, next_element_idx))

    return merged_list

# Приклад використання згідно з описом завдання 
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print(f"Вхідні списки: {lists}")
print(f"Відсортований список: {merged_list}")
