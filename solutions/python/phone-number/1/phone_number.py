import string


class PhoneNumber:
    def _clean(self, input):
        phone_str = str(input)
        legal_punctuation = {"+", "-", "(", ")", " ", "."}
        illegal_punctuation = set(string.punctuation) - legal_punctuation

        # 1. Reject evil punctuation and letters
        for char in phone_str:
            if char in illegal_punctuation:
                raise ValueError("punctuations not permitted")
            if char.isalpha():
                raise ValueError("letters not permitted")

        # 2. Extract the digits
        cleaned_digits = "".join(char for char in phone_str if char.isdigit())

        # 3 Structural length checks( must be 10 or 11)
        if len(cleaned_digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(cleaned_digits) > 11:
            raise ValueError("must not be greater than 11 digits")

        # 4. Handle 11-digit numbers( Trims country code '1')
        if len(cleaned_digits) == 11:
            if cleaned_digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            cleaned_digits = cleaned_digits[1:]

        # 5. Check area code
        if cleaned_digits[0] in ("0", "1"):
            if cleaned_digits[0] == "0":
                raise ValueError("area code cannot start with zero")
            else:
                raise ValueError("area code cannot start with one")

        # 6. Check exchange code
        if cleaned_digits[3] in ("0", "1"):
            if cleaned_digits[3] == "0":
                raise ValueError("exchange code cannot start with zero")
            else:
                raise ValueError("exchange code cannot start with one")
        return cleaned_digits

    def __init__(self, number):
        self.number = self._clean(number)
        self.area_code = self.number[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:10]}"
