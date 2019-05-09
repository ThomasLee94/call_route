def find_index(text: str, pattern: str, start=0) -> (int, None):
    """Return true if there is a match false if not."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # case: pattern is empty
    if len(pattern) == 0:
        return True
    # case: pattern is the text
    if pattern == text:
        return True
    # case: pattern length is greater than text
    if len(pattern) > len(text):
        return False
    # loop through text with pattern
    for index in range(start, len(text) - len(pattern) + 1):
        if text[index] == pattern[0]:
            # once there is a match, if the rest of the pattern after pattern[0] are present, return text_index
            # current index + length of pattern
            if text[index: index+len(pattern)] == pattern:
                return True
    return False
