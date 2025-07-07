from collections import defaultdict, deque


def get_execution_order(jobs: list[str], deps: list[tuple[str, str]]) -> list[str]:
    """
    Returns a list of jobs in a valid execution order.
    Each dependency is a pair (a, b) meaning 'a must run before b'.
    If no valid order exists (i.e., cycle), return an empty list.
    """

    graph = defaultdict(list)
    prereqs = {job: 0 for job in jobs}

    for pre, post in deps:
        graph[pre].append(post)
        prereqs[post] += 1

    # queue of jobs w/ no deps
    queue = deque([job for job in jobs if prereqs[job] == 0])

    result = []

    while queue:
        job = queue.popleft()
        result.append(job)

        for neighbor in graph[job]:
            prereqs[neighbor] -= 1
            if prereqs[neighbor] == 0:
                queue.append(neighbor)
        
    if len(result) == len(jobs):
        return result
    else:
        return []



jobs = ["a", "b", "c", "d"]
deps = [("a", "b"), ("b", "c"), ("a", "d")]

get_execution_order(jobs, deps)  # ➝ ["a", "d", "b", "c"] or ["a", "b", "d", "c"]

