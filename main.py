path_to_file = '/home/gio/workspace/github.com/johnnyhomeless/bookbot/books/frankenstein.txt'

      
def main():
        with open(path_to_file, 'r') as f:
            text = f.read()
        counter = word_counter(text)
        print(f"You have {counter} words")

def word_counter(text):
    return len(text.split())

if __name__ == "__main__":
  main()
