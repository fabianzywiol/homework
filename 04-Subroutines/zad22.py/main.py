import text_analyzer_module

def main():
    text = "You never get a second chance to make a first impression"
    letter_to_count = 'e'
    
    occurrences = text_analyzer_module.count_letter_occurrences(text, letter_to_count)

    print(f"The number of letter '{letter_to_count}': {occurrences}")

if __name__ == "__main__":
    main()
