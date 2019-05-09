#!python

def contains(text: str, pattern: str) -> bool:
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # check if pattern is smaller than text
    if len(pattern) > len(text):
        return False
    # case: pattern is empty
    if len(pattern) == '':
        return True

    text_length = len(text)
    pattern_length = len(pattern)
    counter = 0 

    # loop over text
    for index in range(0, text_length):
        if counter == pattern_length:
            return True
        if text[index] == pattern[0] or text[index] == pattern[counter]:
            counter += 1
        else:
            counter = 0
    if counter == pattern_length:
        return True
    else:
        return False
        
def find_index(text: str, pattern: str, start=0) -> (int, None):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # case: pattern is empty
    if len(pattern) == 0:
        return 0
    # case: pattern is the text
    if pattern == text:
        return 0
    # case: pattern length is greater than text
    if len(pattern) > len(text):
        return None

    # loop through text with pattern
    for index in range(start, len(text) - len(pattern) + 1):
        if text[index] == pattern[0]:
            # once there is a match, if the rest of the pattern after pattern[0] are present, return text_index
            # current index + length of pattern
            if text[index: index+len(pattern)] == pattern:
                return index
    return None
    
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # case: text is equal to pattern
    if text == pattern:
        return [0]
    
    # case: pattern is empty - return all indicies of text
    if pattern == '':
        return [index for index in range(0,len(text))] 
    
    output = []
    found_index = find_index(text, pattern)

    while found_index != None:
        output.append(found_index)
        found_index = find_index(text, pattern, found_index + 1)  
    return output

    
def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
