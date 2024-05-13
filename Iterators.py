
print("List Iteration")
l = ["Python", "web", "scraping"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("python", "web", "scraping")
for i in t:
    print(i)

print("\nString Iteration")
s = "Python"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))
