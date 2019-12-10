string1 = "Today is"
string2 = "A Beautiful day"
txt = string1 + " " + string2

print("{0} {1}".format(string1, string2).lower())
print("%s %s" % (string1.lower(), string2.lower()))
print(txt.casefold())
