from collections import defaultdict


requests = defaultdict(list)

def should_allow(user_id: str, timestamp: int) -> bool:
    # Remove any timestamps older than 60 seconds
    requests[user_id] = [t for t in requests[user_id] if timestamp - t < 60]

    if len(requests[user_id]) < 3:
        requests[user_id].append(timestamp)
        return True
    else:
        return False




should_allow("12313", 1751830486)
