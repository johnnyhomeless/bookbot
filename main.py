path_to_file = 'books/frankenstein.txt'

def main():
    with open(path_to_file, 'r') as f:
        text = f.read()
    counter = word_counter(text)
    print(f"--- Comienza el informe de {path_to_file} ---")
    print(f"Cantidad de palabras: {counter}")
    report(text)
    print("--- Fine del informe ---")

def word_counter(text):
    return len(text.split())

def letter_counter(text):  # Make sure this function accepts text as an argument
    text = text.lower()  # Lowercase the text here
    dict_for_counting = {}
    for char in text:
        if char.isalpha():
            if char in dict_for_counting:
                dict_for_counting[char] += 1
            else:
                dict_for_counting[char] = 1
    return dict_for_counting

def report(text):
    letter_count = letter_counter(text)  # Get letter counts
    letter_count_items = list(letter_count.items())  # Use letter_count instead of dict_for_counting
    sorted_letter_count = sorted(letter_count_items, key=lambda item: item[1], reverse=True)
    for char, count in sorted_letter_count:
        print(f"The '{char}' character was found {count} times")

if __name__ == "__main__":
    main()
