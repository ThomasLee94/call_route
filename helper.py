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

def read_str_dict(file):
    # ! Runtime = O(n), n being the number entries in file
    # ! Memory = O(n), n being the number of entries in file

    ''' Returns a list of phone numbers '''

    dict = {}
    with open(file) as f:
        for line in f:
            (key, value) = line.strip().split(',')
            dict[key] = value
    return dict
