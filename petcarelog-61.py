# === Stage 61: Add performance timing for core list and search operations ===
# Project: PetCareLog
import time


def time_operation(func, *args, repeats=1):
    results = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        results.append((result, end - start))
    return results


def benchmark_list_operations(entries):
    list_result, list_time = time_operation(
        lambda: [e for e in entries if e.get("active", True)], entries
    )[0]
    list_time *= len(entries)
    return list_time


def benchmark_search_operations(entries, search_key="name", search_value=None):
    search_result, search_time = time_operation(
        lambda: [e for e in entries if e.get(search_key) == search_value], entries
    )[0]
    search_time *= len(entries)
    return search_time


def time_all_operations(entries, search_key="name", search_value=None):
    return {
        "list_filter_time": benchmark_list_operations(entries),
        "search_time": benchmark_search_operations(
            entries, search_key, search_value
        ),
    }
