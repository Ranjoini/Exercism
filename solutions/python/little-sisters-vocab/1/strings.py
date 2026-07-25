"""Functions for creating, transforming, and adding prefixes to strings."""
def add_prefix_un(word):
    return 'un' + word 
def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended"""
    prefix = vocab_words[0]
    results = [prefix] + [prefix + word for word in vocab_words[1:]]
    return ' :: '.join(results)
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    root = word[:-4] 
    if root.endswith('i'):
        return root[:-1] + 'y'
    return root 
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()
    adjective = words[index]
    verb = adjective.strip(". , !")
    return verb + 'en'
    
    
