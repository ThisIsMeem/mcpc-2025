
#ThisIsMeem
# Problem: Find the word that appears most consecutively


# Read a line of text from input
line = input().strip()

# Split the line into words
words = line.split()

# Initialize variables to track the best word so far
best_word = words[0]      # word with the longest consecutive streak
best_count = 1            # length of the longest streak
current_word = words[0]   # current word being counted
current_count = 1         # streak length of the current word

# Loop through all words starting from the second
for i in range(1, len(words)):
    w = words[i]

    if w == current_word:
        # Same as previous, increase current streak
        current_count += 1
    else:
        # New word, reset current streak
        current_word = w
        current_count = 1

    # Update best if current streak is longer
    if current_count > best_count:
        best_count = current_count
        best_word = current_word

# Print the result
print(best_word)
