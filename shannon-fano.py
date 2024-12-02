# Function to generate Shannon-Fano codes
def shannon_fano(symbols, freqs):
    # Base case: If only one symbol is left, it gets the code '0'
    if len(symbols) == 1:
        return {symbols[0]: '0'}

    # Sort symbols based on frequency (highest to lowest)
    sorted_pairs = sorted(zip(symbols, freqs), key=lambda x: x[1], reverse=True)
    symbols, freqs = zip(*sorted_pairs)

    # Find the index to split the list of symbols into two roughly equal parts
    total_freq = sum(freqs)
    running_freq = 0
    split_index = 0

    # Split the symbols in such a way that the frequencies are as balanced as possible
    for i in range(len(freqs)):
        running_freq += freqs[i]
        if running_freq >= total_freq / 2:
            split_index = i + 1
            break

    # Divide symbols and frequencies into two parts
    left_symbols = symbols[:split_index]
    right_symbols = symbols[split_index:]
    left_freqs = freqs[:split_index]
    right_freqs = freqs[split_index:]

    # Recursively generate codes for the left and right parts
    left_codes = shannon_fano(left_symbols, left_freqs)
    right_codes = shannon_fano(right_symbols, right_freqs)

    # Add '0' to the left codes and '1' to the right codes
    codes = {**{symbol: '0' + code for symbol, code in left_codes.items()},
             **{symbol: '1' + code for symbol, code in right_codes.items()}}

    return codes

# Example usage
if __name__ == "__main__":
    symbols = ['A', 'B', 'C', 'D', 'E', 'F']
    frequencies = [5, 9, 12, 13, 16, 45]

    # Generate Shannon-Fano codes
    codes = shannon_fano(symbols, frequencies)

    # Print the codes
    print("Shannon-Fano Codes:")
    for symbol, code in codes.items():
        print(f"{symbol}: {code}")
