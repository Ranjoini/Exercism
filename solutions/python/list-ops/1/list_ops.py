def append(list1, list2):
    return list1 + list2


def concat(lists):
    flat_list = []
    for inner_list in lists:
        flat_list.extend(inner_list)
    return flat_list


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for item in list[::-1]:
        accumulator = function(accumulator, item)
    return accumulator


def reverse(list):
    return list[::-1]
