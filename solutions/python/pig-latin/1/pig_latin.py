VOWELS = ("a", "e", "i", "o", "u")
SPECIAL_PREFIXES = ("xr", "yt")


def translate(text: str) -> str:
    """Translate a string of English words into Pig Latin."""

    words = text.split()
    processed_words = []

    for word in words:
        # --- RULE 1: Vowels and Special Prefixes ---
        if word.startswith(VOWELS) or word.startswith(SPECIAL_PREFIXES):
            new_word = word + "ay"
            processed_words.append(new_word)

        # --- RULES 2, 3, & 4: Consonants, "qu", and "y" ---
        else:
            vowel_index = 0

            # The Scanner
            for letter in word:
                if letter in VOWELS:
                    break
                if letter == "y" and vowel_index > 0:  # Rule 4: 'y' acts as a vowel
                    break
                vowel_index += 1

            # Rule 3: The "qu" override
            if (
                vowel_index > 0
                and word[vowel_index] == "u"
                and word[vowel_index - 1] == "q"
            ):
                vowel_index += 1

            # The Slicer and Reassembly
            consonants = word[:vowel_index]
            rest_of_word = word[vowel_index:]

            new_word = rest_of_word + consonants + "ay"
            processed_words.append(new_word)

    return " ".join(processed_words)
