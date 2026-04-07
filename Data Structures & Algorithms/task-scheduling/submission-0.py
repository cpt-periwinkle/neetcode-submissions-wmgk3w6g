import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ---------------- CORE IDEA ----------------
        # We want to schedule tasks with a cooldown of n between same tasks.
        #
        # Strategy:
        # 1. Always execute the task with the highest remaining frequency
        #    → greedy choice
        # 2. Use a MAX HEAP to always pick the most frequent task
        # 3. Use a queue to track tasks that are in cooldown

        # Count frequency of each task
        cnt = Counter(tasks)

        # Max heap (use negative values since Python has min heap)
        # Each value represents how many times a task still needs to run
        max_heap = [-count for count in cnt.values()]
        heapq.heapify(max_heap)

        # time = current time unit (each loop = 1 unit)
        time = 0

        # Queue stores tasks that are cooling down
        # Each entry: [remaining_count, time_when_available]
        q = deque()

        # Run until no tasks left in heap AND no tasks cooling down
        while max_heap or q:
            time += 1  # move forward in time

            # ---------------- CASE 1: HEAP EMPTY ----------------
            # No task can be executed right now → idle
            if not max_heap:
                # Jump time forward to when next task becomes available
                # (optimization instead of incrementing one by one)
                time = q[0][1]

            else:
                # ---------------- CASE 2: EXECUTE TASK ----------------
                # Pick the most frequent task
                count = 1 + heapq.heappop(max_heap)

                # Why "1 + ..."?
                # Because values are negative:
                # e.g. -3 → after one execution becomes -2

                # If task still has remaining executions
                if count:
                    # Put it into cooldown queue
                    # It will be available again at time + n
                    q.append([count, time + n])

            # ---------------- CHECK COOLDOWN ----------------
            # If any task has completed cooldown, push it back into heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time