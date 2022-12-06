# Count a specific pattern in a text/dna seq

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

# Frequency, parameter k ={1,...N} in a text/dna seq

def Frequency(text, k):
    freq = {}
    foo = len(text)
    for i in range(foo-k+1):
        pattern = text[i:i+k]
        if pattern in freq:
            freq[pattern] += 1
            continue
        else:
            freq[pattern] = 1
    return freq

# Find the k-seq with the most frequency in a text/dna seq

def MaxFreq(text, k):
    patterns = []
    freq = Frequency(text, k)
    all_values = freq.values()
    max_value = max(all_values)
    for key in freq:
        if freq[key] == max_value:
            patterns.append(key)
    return patterns

# starting positions in Genome where Pattern appears as a substring

def find_start_pos(pattern, genome):
    """alternative way of finding starting pos"""
    # pos = 0
    # while True:
    #     pos = genome.find(pattern, pos)
    #     if pos == -1: return
    #     yield pos
    #     pos += 1
    index = [i for i in range(len(genome)) if genome.startswith(pattern, i)]
    return index


text = "GATATATGCATATACTT"
k = 4
pattern = "ATAT"
print(find_start_pos("ATAT", "GATATATGCATATACTT"))