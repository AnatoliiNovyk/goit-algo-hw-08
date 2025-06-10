import heapq
from typing import List, Tuple

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків в один відсортований список.

    Args:
        lists (List[List[int]]): Список відсортованих списків.

    Returns:
        List[int]: Один об'єднаний відсортований список.
        
    Часова складність: O(N log k), де N - загальна кількість елементів, 
                      а k - кількість списків.
    Просторова складність: O(k) для зберігання купи.
    """
    # Підказки типів для змінних для кращої читабельності
    min_heap: List[Tuple[int, int, int]] = []
    
    for i, lst in enumerate(lists):
        if lst:
            # (значення, індекс_списку, індекс_елемента)
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list: List[int] = []

    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        
        merged_list.append(value)

        if element_idx + 1 < len(lists[list_idx]):
            next_element_idx = element_idx + 1
            next_value = lists[list_idx][next_element_idx]
            heapq.heappush(min_heap, (next_value, list_idx, next_element_idx))

    return merged_list

# Приклад використання
lists_to_merge = [[1, 4, 5], [1, 3, 4], [2, 6]]
final_list = merge_k_lists(lists_to_merge)

print(f"Вхідні списки: {lists_to_merge}")
print(f"Відсортований список: {final_list}")
