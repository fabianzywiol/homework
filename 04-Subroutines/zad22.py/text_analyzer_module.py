def count_letter_occurrences(text, letter):
    count = 0
    for char in text:
        if char.lower() == letter.lower():
            count += 1
    return count

