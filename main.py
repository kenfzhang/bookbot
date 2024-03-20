def sort_on(d):
  return d["num"]

def get_sorted_letter_list(char_counts):
  # Create list of dictionaries w/ letter: count
  letters_by_count = []
  for i in char_counts:
    if i.isalpha():
      lbc = {}
      lbc["name"] = i
      lbc["num"] = char_counts[i]
      letters_by_count.append(lbc)
  # Sort by count and return list
  letters_by_count.sort(reverse=True, key=sort_on)
  return letters_by_count

def report(path):
  text = get_book_text(path)
  words = word_count(text)
  char_counts = count_chars(text)
  print(f'--- Report of {path} ---')
  print(f'Document contains {words} words')
  print()
  print("Frequency of each letter:")
  letters_by_count = get_sorted_letter_list(char_counts)
  for l in letters_by_count:
    print(f'{l["name"]}: {l["num"]}')
  print('--- End report ---')

def count_chars(text):
  counts = {}
  for i in text:
    i_l = i.lower()
    if i_l not in counts:
      counts[i_l] = 1
    else:
      counts[i_l] += 1
  return counts

def word_count(text):
  return len(text.split())

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
    return file_contents

def main():
  report('./books/frankenstein.txt')

if __name__ == '__main__':
  main()
