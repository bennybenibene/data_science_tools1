"""regular expressions (RegEx)

Regular expressions are used to search a string for a specified sequence of characters
that serve as a search pattern.  Python has a built-in module called re to work
with such expressions.
"""

import re

"""findall(), search(), split() and sub() are useful re functions.

Initially we'll be using the top-level versions of these function.
Towards the end of the demo we will use re.compile() to create pattern objects and invoke these same methods.
"""

# an example string:
text = 'The dog was running fast today.'

# findall() returns a list containing all matches
print(re.findall("[a-g]", text))
print(re.findall("[a-zA-Z]", text))

# search() returns a re match object. If no matches are found then None is returned.
print(re.search("^Hello", text))
print(re.search("^The", text))

# match objects have some special methods and attributes.
# for example:
x = re.search("running", text)

# x. string returns the passed string
print(x.string)

# .span() will return a tuple with start and end indices of the match within the original string
print(x.span())
# .start() and .end() return beginning and ending indices, respectively

x.string[x.start(): x.end()]

# split() will return a list where the input string has been split on the match occurrence
text = 'Today I walked the dog and I ate breakfast and I worked.'
print(re.split(" I ", text))

# sub() will replace one or more matches with a specified string and return the substituted string.
x = re.sub('I', 'you', text)
print(x)

"""Metacharacters:

re utilizes metacharacters, which are just characters that have a unique meaning
in the context of the module. They are as follows.
. ^ $ * + ? {} [] \ | ()
"""

# []
# brackets are used to specify a character class (a set of characters).
text = 'zzv$AbabB$$cddRrty$Hi'
print(re.findall("[a-d]", text))

# same as:
print(re.findall("[abcd]", text))

# note that metacharacters are stripped of their meaning inside of a character class,
# so below $ is now treated as a character not a metacharacter
print(re.findall("[abcd$]", text))

# you can take the compliment of the set by using ^ as the first element of the character class.
# if ^ is in any other than the first position of the class it will be treated as the caret character.
# for example, the following will have the same result.
text = '^hello^world^'
print(re.findall("[a-z]", text))
print(re.findall("[^^]", text))

# \
# indicates a special sequence or will escape characters.
# re has several special sequences which are referenced using a backslash as the first character.
text = 'I[want[to[find[left[brackets'
print(re.findall("\[", text))

# .
# Represents any character except a newline character
# notice the results below.
text = '\n\nTrying||\tto find a matches.\n'
print(re.findall("...[a-b]..", text))

# ^
# starts with
text = 'Today I walked the dog and I ate breakfast and I worked.'
print(re.findall("^Today", text))

# notice the significantly different result we get when making a character class out of
# the elements in the preceding RE
print(re.findall("[^Today]", text))

# $
# ends with
# here we escape the .
print(re.search("worked\.$", text))

# *
# matches zero or more occurences
text = '12 b34 a85 99 j65 100 z t999 wi876'
print(re.findall("[a-z][0123456789]*", text))

# +
# matches one or more occurences
print(re.findall("[a-z]+[0123456789]+", text))

# ?
# mathces zero or one occurences
print(re.findall("[a-z]?[0123456789]+", text))

# {}
# exact number of occurences
print(re.findall("[a-z]{1}[0123456789]{2}", text))

# |
# either or
text_1 = 'yeah it was fun yes it was'
text_2 = 'yes it was fun'

print(re.findall("yeah|yes", text_1))
print(re.findall("yeah|yes", text_2))

# ()
# grouping

text = 'abcabcabcabc'
# Here we'll match zero or more repetitions of the sequence abc
print(re.match("(abc)*", text))

""" special sequences

The following special sequences can be used to match elements.
"""

# \b
# this is a zero width assertion. It says that the start position of the match is located at a word boundry
text_1 = "Some thing"
text_2 = "Something"
print(re.search(r"\bthing\b", text_1))
print(re.search(r"\bthing\b", text_2))

# \w
# mathces any alphanumeric character.  This is equivalent to the class [a-zA-Z0-9_]
text = '$$ Here is a short_string.'
print(re.findall("[a-zA-Z0-9_]", text))
print(re.findall("\w", text))

# \W matches any NON-alphanumeric character. This is equivalent to [^a-zA-Z0-9_]
print(re.findall("[^a-zA-Z0-9_]", text))
print(re.findall("\W", text))

# \d
# mathces any decimal digit. This is equivalent to the class [0-9]
text = 'A number555isin123here1234 &&&'
print(re.findall("\d", text))

# \D
# mathces any non-digit character. This is equivalent to the class [^0-9]
print(re.findall("\D", text))

# \s
# matches any whitespace character. This is equivalent to the class [ \t\n\r\f\v]
# note \r is carriage return. \v is ASCII vertical tab, \f is ASCII formfeed (page break)
text = 'A\n\t     string\t\t\t with    space.\n'
print(re.findall("\s", text))
print(re.findall("\s{5}", text))

# \S
# mathces any non-whitespace character. Equivalent to the class [^ \t\n\r\f\v]
print(re.findall("\S", text))

# special sequences can be used inside character classes
# say we want to match any white space and dollar signs or question marks
text = '   Here is $1 worth of words words.'
print(re.findall("[\s$]", text))

# Repetition

# the metacharacter * allows you to specify repetition of elements within your regular expression
# * matches zero or more times
text = 'apple orange banana kiwi lemon'

print(re.findall("[aeiou][a-z]*[aeiou]", text))
print(re.findall("[aeiou]*[a-z]*[aeiou]", text))

# + is another repetition character
# it matches one or more times.  There is a subtle but important difference between * and +

# also ? matches zero or one occurrences

# finally, {m,n} where m and n are integers, matches cases where there are at least m repetitions and at most n

# for example:
text = 'hello helllo hellllo helllllllllo HeLlO'
print(re.findall("hel{2,3}o", text))

# the compile method allows us to compile REs into pattern objects and use them for matching
# the re objects have various methods themselves.
# REs are handled as strings in Python in order to simplify the language and not require additional
# syntax dedicated to regular expressions.

p = re.compile("hel{2,3}o")
print(p.findall(text))

# re.compile() accepts flag arguments.  For example:
r = re.compile("hel{2,3}o", re.IGNORECASE)
print(r.findall(text))

# Back to methods and attributes of pattern objects. These are the core methods...there are more.

# match() determines if the RE matches the beginning of the string and
# returns None if no match can be found
# if it is successful then a match object instance is returned

# search() assesses the entire string look for any location where the RE matches
# returns None if no match can be found
# if it is successful then a match object instance is returned

# findall() will find all substrings where the RE matches and
# returns them as a list

# finditer() will find all substrings where the RE matches and
# returns them as a sequence of match object instances as an iterator

text = 'foo'
# this pattern object won't find a match in the above string
p = re.compile("o+")
print(p.match(text))

# now we're looking for one or more f chars at the beginning of the string
p = re.compile("f+")
print(p.match(text))

text = '     abc'
# here the beginning of the string is several space characters
p = re.compile("[a-z]+")
print(p.match(text))

# now we're trying to match one or more space chars at the beginning of the string
p = re.compile("\s+")
# we should find a match here...let's assign the match object to a variable
m = p.match(text)

# the match object has several methods
m.group() # returns matched substring

m.start() # returns starting index of substring. start should always be 0 with match()
m.end() # returns starting index of substring
m.span() # returns start and end as a tuple

# defining a new RE

p = re.compile("[a-zA-Z ]+")

# this won't match anything
print(p.match('::::Some Text'))

m = p.search('::::Some Text')
print(m)
print(m.group()) # returns substring
print(m.span())

# A common way to check if you've found a match is as follows
p = re.compile("\d+")
m = p.search('2345 4578 87632 78374')

if m:
    print("Match(es) found: ", m.group())
else:
    print('No matches')

# note that search and match will only return the first match object instance.
# suppose we want to find all of the matches above
m_list = p.findall('2345 4578 87632 78374')
print(m_list)

for match in m_list:
    print(match)

iterator = p.finditer('2345 4578 87632 78374')
print(iterator)

for match in iterator:
    print(match.group())
    print(match.span())
