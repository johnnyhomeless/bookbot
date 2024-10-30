path_to_file = 'books/frankenstein.txt'
      
def main():
        with open(path_to_file, 'r') as f:
            text = f.read()
        counter = word_counter(text)
        print(f"Cantidad de palabras: {counter}")

def word_counter(text):
    return len(text.split())

def letter_counter():
    with open(path_to_file, 'r') as f:
        text = f.read().lower()
    dict_for_counting = {}
    for char in text:
        if char.isalpha():
            if char in dict_for_counting:
              dict_for_counting[char] += 1
            else:
               dict_for_counting[char] = 1
    return dict_for_counting


if __name__ == "__main__":
  main()
  print(letter_counter())

