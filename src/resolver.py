import json


def question_1(param):
    """
    Receives an array as parameter and works it to return only one number.
    :param param:
    :return:
    """
    array = json.loads(param)
    numbers_list = [i for i in array if isinstance(i, int)]
    higher = max(numbers_list)
    numbers_list.remove(higher)
    result = higher + max(numbers_list)
    return result


def question_2(param):
    """
    Receives an string with brackets and solves if it is in order with open
    and closed ones or not, returning a boolean.
    :param param:
    :return:
    """
    if param:
        brackets = ['()', '{}', '[]']
        bracket_copy = param
        checklist = ['{', '}', '[', ']', '(', ')']
        for check in checklist:
            if check in bracket_copy:
                bracket_copy = bracket_copy.replace(check, '')
        if bracket_copy:
            raise TypeError
        while any(x in param for x in brackets):
            for br in brackets:
                param = param.replace(br, '')
        return not param
    else:
        raise TypeError


def question_3(param):
    """
    Receives an array as a parameter and return a phrase based on the array
    given by the user, like buying actions in trade and selling at its highest
    return the maximum value in order of days if there is a profit.
    :param param:
    :return:
    """
    array = json.loads(param)
    numbers_list = [i for i in array if isinstance(i, int)]
    first, second, total = 0, 0, 0
    for n in range(len(numbers_list)):
        pos, val = min(enumerate(numbers_list), key=(lambda x: x[1]))
        if pos+1 < len(numbers_list):
            for number in range(pos+1, len(numbers_list)):
                if numbers_list[number] - val > total:
                    first = val
                    second = numbers_list[number]
                    total = second - first
        numbers_list.remove(val)
    if total > 0:
        formated_answer = f"{total} (Comprou no dia {array.index(first) + 1} " \
                          f"(preço igual a {first}) e vendeu no dia " \
                          f"{array.index(second) + 1} (preço igual a " \
                          f"{second}), lucro foi de {second} - {first} = " \
                          f"{total}"
    else:
        formated_answer = '0 (Nesse caso nenhuma transação deve ser feita, ' \
                          'lucro máximo igual a 0)'
    return formated_answer


def question_4(param):
    """
    Receives an array as parameter and builds it like it's a graph, numbers
    given becomes 'rocks' in a straight line from bottom to the top and any
    space between becomes like a pool where water is gathered, return the
    exact amount of blocks that were empty and would gather water.
    :param param:
    :return:
    """
    array = json.loads(param)
    barrage = [i for i in array if isinstance(i, int)]
    water, counter = 0, 0
    stack = []
    while counter < len(barrage):
        if len(stack) == 0 or barrage[stack[-1]] >= barrage[counter]:
            stack.append(counter)
            counter += 1
        else:
            x = stack[-1]
            stack.pop()
            if len(stack) != 0:
                minimum = min(barrage[stack[-1]], barrage[counter])
                distance = counter - stack[-1]-1
                water += distance*(minimum - barrage[x])
    return water
