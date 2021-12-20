"""
* Assignment: Loop For Text
* Required: no
* Complexity: medium
* Lines of code: 14 lines
* Time: 13 min

English:
    1. Given is text of the "Moon Speech" by John F. Kennedy's [1]
    2. Sentences are separated by period (`.`)
    3. Clean each sentence from whitespaces at the beginning and at the end
    4. Words are separated by spaces
    5. Print the total number in whole text:
        a. adverbs (words ending with "ly")
        b. sentences
        c. words
        d. letters
        e. characters (including spaces inside sentences, but not comas `,`)
        f. comas (`,`)
    6. Run doctests - all must succeed

Polish:
    1. Dany jest tekst przemówienia "Moon Speech" wygłoszonej
       przez John F. Kennedy'ego [1]
    2. Zdania oddzielone są kropkami (`.`)
    3. Każde zdanie oczyść z białych znaków na początku i końcu
    4. Słowa oddzielone są spacjami
    5. Wypisz także ile jest łącznie w całym tekście:
        a. przysłówków (słów zakończonych na "ly")
        b. zdań
        c. słów
        d. liter
        e. znaków (łącznie ze spacjami wewnątrz zdań, ale bez przecinków `,`)
        f. przecinków (`,`)
    6. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Kennedy, J.F. Moon Speech - Rice Stadium.
        Year: 1962.
        Retrieved: 2021-03-06.
        URL: http://er.jsc.nasa.gov/seh/ricetalk.htm

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>

    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    {'sentences': 7,
     'words': 71,
     'characters': 347,
     'letters': 283,
     'commas': 1,
     'adverbs': 0}
"""

TEXT = """
    We choose to go to the Moon.
    We choose to go to the Moon in this decade and do the other things.
    Not because they are easy, but because they are hard.
    Because that goal will serve to organize and measure the best of our energies and skills.
    Because that challenge is one that we are willing to accept.
    One we are unwilling to postpone.
    And one we intend to win
"""

# dict[str,int]: number of occurrences of each grammar object
result = {
    'sentences': 0,
    'words': 0,
    'characters': 0,
    'letters': 0,
    'commas': 0,
    'adverbs': 0,
}
