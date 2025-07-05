# Hashmap basic use
counts = {}
for ch in 'interview':
    counts[ch] = counts.get(ch, 0) + 1
