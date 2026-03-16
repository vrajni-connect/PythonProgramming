def capitalize_words(s):
    """Capitalize the first letter of each word in the string."""
    return ' '.join(word.capitalize() for word in s.split())

def reverse_string(s):    
    """Reverse the given string."""
    return s[::-1]  

def word_count(s):
    """Count the number of words in the string."""
    return len(s.split())   
