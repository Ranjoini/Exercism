class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        clean_num = self.card_num.replace(" ", "")
        if len(clean_num) <= 1 or not clean_num.isdigit():
            return False
        total = 0
        for i, char in enumerate(reversed(clean_num)):
            d = int(char)
            if i % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            total += d
        return total % 10 == 0
