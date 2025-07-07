from collections import defaultdict
import json


def Initialize(queries: list[str], counts: list[int]):
    frequency_array = defaultdict(list)
    for query, count in zip(queries, counts):
        frequency_array[count].append(query)

    print(json.dumps(frequency_array, indent=2))


Initialize(["rm 123.txt", "rm 456.txt", "ls -la", "blah blah blah"], [4, 5, 1, 4])

def input(char: str) -> list[str]:
    