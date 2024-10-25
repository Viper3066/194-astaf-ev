def normalize_list(a):
    min_val = min(a)
    max_val = max(a)
    if min_val == max_val:
        return [0.0] * len(a)
    n_a = [(x - min_val) / (max_val - min_val) for x in a]
    return n_a
a = [2, 4, 10, 6, 8, 4]
normalized_a = normalize_list(a)
print("Нормализованный список:", normalized_a)
