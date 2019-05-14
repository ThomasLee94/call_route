def read_str_dict(file):
    # ! Runtime = O(n), n being the number entries in file
    # ! Memory = O(n), n being the number of entries in file

    ''' Returns prefix and cost as a dict '''

    dict = {}
    with open(file) as f:
        for line in f:
            (key, value) = line.strip().split(',')
            dict[key] = value
    return dict

def read_str_list(file):
    with open(file) as f:
        # generator for [(prefix, cost),(prefix,cost)...] - does not get built immediately 
        lines = (l.split(',') for l in f.readlines())
    return lines

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

    

