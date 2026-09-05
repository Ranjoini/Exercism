class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    custom_words = {}

    def pop_two():
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        val_b = stack.pop()
        val_a = stack.pop()
        return val_a, val_b

    def check_one():
        if len(stack) < 1:
            raise StackUnderflowError("Insufficient number of items in stack")

    for data in input_data:
        tokens = data.lower().split()
        if tokens[0] == ":" and tokens[-1] == ";":
            new_word_name = tokens[1]
            try:
                int(new_word_name)
            except ValueError:
                pass
            else:
                raise ValueError("illegal operation")
            raw_definition = tokens[2:-1]
            expanded_definition = []
            for token in raw_definition:
                if token in custom_words:
                    expanded_definition.extend(custom_words[token])
                else:
                    expanded_definition.append(token)
            custom_words[new_word_name] = expanded_definition
            continue
        executable_line = []
        for token in tokens:
            if token in custom_words:
                executable_line.extend(custom_words[token])
            else:
                executable_line.append(token)

        def op_div():
            a, b = pop_two()
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)

        def op_dup():
            check_one()
            stack.append(stack[-1])

        def op_drop():
            check_one()
            stack.pop()

        def op_swap():
            a, b = pop_two()
            stack.extend([b, a])

        def op_over():
            if len(stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            stack.append(stack[-2])

        def op_sub():
            a, b = pop_two()
            stack.append(a - b)

        def op_mul():
            a, b = pop_two()
            stack.append(a * b)

        operations = {
            "+": lambda: stack.append(sum(pop_two())),
            "-": op_sub,
            "*": op_mul,
            "/": op_div,
            "dup": op_dup,
            "drop": op_drop,
            "swap": op_swap,
            "over": op_over,
        }
        for token in executable_line:
            try:
                stack.append(int(token))
                continue
            except ValueError:
                pass
            action = operations.get(token)
            if action:
                action()
            else:
                raise ValueError("undefined operation")
    return stack
