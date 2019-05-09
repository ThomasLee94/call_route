def find_all_indexes(text, pattern):
    """Return a list of all occurrences of pattern in text,
    or an empty list if none found."""
    
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