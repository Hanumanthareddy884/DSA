myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

d = list(map(lambda a:myfamily[a]['name'],myfamily))
print(d)
# a = list(map(lambda a:myfamily[a].keys(),myfamily))
# print(a)

