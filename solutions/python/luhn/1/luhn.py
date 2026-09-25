class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        clean_num = self.card_num.replace(" ", "")
        if len(clean_num) <= 1 or not clean_num.isdigit():
            return False
        digit = [int(c) for c in clean_num[::-1]]
        untouched = digit[0::2]
        to_double = digit[1::2]
        doubled = [d * 2 - 9 if d * 2 > 9 else d * 2 for d in to_double]
        total = sum(untouched) + sum(doubled)
        return total % 10 == 0
