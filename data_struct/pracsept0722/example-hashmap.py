#hashtable

class hashmap:
    def __init__(self):
        self.size = 20
        self.ht = [[] for _ in range(0, self.size)]



h = hashmap()


h.set("big_house", "martell")
h.set("med_house", "tony")
h.set("small_house", "emma")

print(h.ht)




