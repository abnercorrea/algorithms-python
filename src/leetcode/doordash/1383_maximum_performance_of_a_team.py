from typing import List


def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    def max_perf_rec(start: int, size: int, total_speed: int, min_eff: int, max_perf: int):
        if size == k:
            return max_perf

        for i in range(start, n):
            new_total_speed = total_speed + speed[i]
            new_min_eff = min(efficiency[i], min_eff)
            max_perf = max(new_total_speed * new_min_eff, max_perf_rec(i + 1, size + 1, new_total_speed, new_min_eff, max_perf))

        return max_perf

    return max_perf_rec(0, 0, 0, 10 ** 8, 0)
