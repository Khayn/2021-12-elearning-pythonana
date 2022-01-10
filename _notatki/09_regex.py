#%% Regex

# Wyrażenia regularne
# Regular Expressions
# Re
# Regex
# Regexp

# %% Więcej informacji

# https://www.youtube.com/watch?v=BmF-gEYXWVM&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=3
# https://python.astrotech.io/intermediate/_index.html#regular-expressions


# %% Use Case
import re


phone1 = '+48 123 456 789'
phone2 = '+48 (12) 345-6789'

a = re.findall('[0-9]', phone1)
b = re.findall('[0-9]', phone2)

a == b
# True



TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

# Qualifier
# Identifier
# Negation
# Quantifier
# Grouping
# Flags


'(?P<month>\w{3}) (?P<day>\d{1,2})(?:st|nd|rd|th), (?P<year>\d{4})'

# \d - [0-9]
# \w - [a-zA-Z0-9ąćśźłó]

# group
# (?:st|nd|rd|th) - non matching group


# (...) positional group
# (?P<nazwa_zmiennej>...) - keyword group
# (?:...) non matching group
# (?#...) comment
