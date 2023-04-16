# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    
    inputted_text = input().strip().lower()
    if inputted_text == "f":
        file_path = "./tests/06"
        with open(file_path, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    elif inputted_text == "i":
        pattern = input().rstrip()
        text = input().rstrip()
    # after input type choice
        
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    occurrences = []
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_len]:
            occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = hash(text[i+1:i+1+pattern_len])
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

