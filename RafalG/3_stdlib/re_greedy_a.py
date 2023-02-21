"""
* Assignment: RE Qualifier Lazy
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Using `re.findall()` and lazy qualifier split text by paragraphs
    2. In `result: str` catch paragraf starting with "We choose to go to the moon"
    3. Run doctests - all must succeed

Polish:
    1. Używając `re.findall()` i lazy qualifier podziel tekst na paragrafy
    2. W `result: str` uchwyć paragraf zaczynający się od słów "We choose to go to the moon"
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * All HTML paragraphs starts with `<p>` and ends with `</p>`
    * In real life paragraphs parsing is more complex
    * You can iterate over the results of `re.findall()`

Test:
    >>> assert type(result) is str, 'result must be a str'
    >>> assert not result.startswith('<p>'), 'result cannot start with <p>'
    >>> assert not result.endswith('</p>'), 'result cannot end with </p>'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    'We choose to go to the moon. We choose to go to the moon in this decade
     and do the other things, not because they are easy, but because they are
     hard, because that goal will serve to organize and measure the best of our
     energies and skills,because that challenge is one that we are willing to
     accept, one we are unwilling to postpone, and one which we intend to
     win, and the others, too.'
"""

import re

TEXT = ("<h1>TEXT OF PRESIDENT JOHN KENNEDY'S RICE STADIUM MOON SPEECH</h1>\n"
        "<p>President Pitzer, Mr. Vice President, Governor, "
        "CongressmanThomas, Senator Wiley, and Congressman Miller, Mr. Webb, "
        "Mr.Bell, scientists, distinguished guests, and ladies and "
        "gentlemen:</p><p>We choose to go to the moon. We choose to go to "
        "the moon in this decade and do the other things, not because they "
        "are easy, but because they are hard, because that goal will serve "
        "to organize and measure the best of our energies and skills,because "
        "that challenge is one that we are willing to accept, one we are "
        "unwilling to postpone, and one which we intend to win, and the "
        "others, too.</p><p>It is for these reasons that I regard the "
        "decision last year to shift our efforts in space from low to high "
        "gear as among the most important decisions that will be made during "
        "my incumbency in the office of the Presidency.</p><p>In the last 24 "
        "hours we have seen facilities now being created for the greatest "
        "and most complex exploration in man's history.We have felt the "
        "ground shake and the air shattered by the testing of a Saturn C-1 "
        "booster rocket, many times as powerful as the Atlas which launched "
        "John Glenn, generating power equivalent to 10,000 automobiles with "
        "their accelerators on the floor.We have seen the site where the F-1 "
        "rocket engines, each one as powerful as all eight engines of the "
        "Saturn combined, will be clustered together to make the advanced "
        "Saturn missile, assembled in a new building to be built at Cape "
        "Canaveral as tall as a48 story structure, as wide as a city block, "
        "and as long as two lengths of this field.</p>")


# str: use findall() and non-greedy qualifier to get paragraph "We choose..."
result = ""

# PATTERN = r"<.*?>"  # with <h1>, </h1>
PATTERN = r"<p>(.*?)</p>"

for paragraph in re.split(PATTERN, TEXT):
    if paragraph.startswith("We choose to go"):
        result += paragraph
