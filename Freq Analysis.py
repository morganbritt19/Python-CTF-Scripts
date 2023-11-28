# This script will perform frequency analysis on a supplied text 
# This can be leveraged to break basic substitution ciphers

from collections import Counter

def frequency_analysis(text):
    freq_counter = Counter(text)
    sorted_freq = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq
