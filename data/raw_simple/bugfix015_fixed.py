def to_title_case(sentence):
    """Convert a sentence to simple title case (first letter of each word)."""
    words = sentence.split(" ")
    result_words = []
    for w in words:
        if not w:
            # preserve empty segments to keep spacing
            result_words.append("")
        else:
            result_words.append(w[0].upper() + w[1:])
    return " ".join(result_words)
