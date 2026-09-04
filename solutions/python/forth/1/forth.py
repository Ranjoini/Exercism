class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    custom_words = {}

    def check_stack(required_length):
        if len(stack) < required_length:
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

        for token in executable_line:
            try:
                number = int(token)
                stack.append(number)
                continue
            except ValueError:
                pass
            if token == "+":
                check_stack(2)
                val_b = stack.pop()
                val_a = stack.pop()
                stack.append(val_a + val_b)
            elif token == "-":
                check_stack(2)
                val_b = stack.pop()
                val_a = stack.pop()
                stack.append(val_a - val_b)
            elif token == "*":
                check_stack(2)
                val_b = stack.pop()
                val_a = stack.pop()
                stack.append(val_a * val_b)
            elif token == "/":
                check_stack(2)
                val_b = stack.pop()
                if val_b == 0:
                    raise ZeroDivisionError("divide by zero")
                val_a = stack.pop()
                stack.append(val_a // val_b)

            elif token == "dup":
                check_stack(1)
                stack.append(stack[-1])

            elif token == "drop":
                check_stack(1)
                stack.pop()

            elif token == "swap":
                check_stack(2)
                val_b = stack.pop()
                val_a = stack.pop()
                # Pushing B first, then A, perfectly reverses their order on the stack
                stack.append(val_b)
                stack.append(val_a)

            elif token == "over":
                check_stack(2)
                # stack[-2] reaches past the top board to grab a copy of the second one
                stack.append(stack[-2])
            else:
                raise ValueError("undefined operation")
    return stack
