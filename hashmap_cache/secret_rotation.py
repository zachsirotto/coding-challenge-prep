import heapq
from typing import Optional


class SecretManager:
    def __init__(self):
        self.heap = []
        self.active = set()

    def add_secret(self, secret_id: str, expires_at: int):
        pair = (secret_id, expires_at)
        heapq.heappush(self.heap, pair)
        self.active.add(pair)

    def get_next_secret(self, now: int) -> Optional[str]:
        # remove non-active secrets
        while self.heap:
            secret_id, expires_at = self.heap[0]
            if expires_at <= now:
                heapq.heappop(self.heap)
            else:
                return secret_id
        return None

    


# Requirements:
# Each secret has an expiration timestamp (epoch seconds).

# get_next_secret(now) should return the next unexpired secret that expires soonest.

# This operation must be efficient (preferably O(log n)).

# Expired secrets should be skipped/cleaned.