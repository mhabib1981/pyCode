import re
myString = "This is my tweet check it out http:// tinyurl.com/blah"
print re.search("(?P<url>http?://[^\s]+)", myString)
