#Task1
def family(name):
    Family = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid"
    }

    if name in Family:
        return f"Luke, I am your {Family[name]}."
    else:
        return "Error."


print(family("Darth Vader"))  # ---> "Luke, I am your father."
print(family("Leia"))  # ---> "Luke, I am your sister."
print(family("Han"))  # ---> "Luke, I am your brother, in law."

#Task2
def mood_today(mood):
    if mood == "neutral":
        return "Today i am feeling neutral"
    else:
        return "Today i am feeling " + mood


print(mood_today("happy"))
print(mood_today("sad"))
print(mood_today("neutral"))

#
# #Task3
def count_vowels(txt):
    lstk = "aeiouAEIOU"
    count = 0
    for x in txt:
        if x in lstk:
            count += 1
    return count


print(count_vowels("Celebration")) #---> 5

print(count_vowels("Palm")) #--->1

print(count_vowels("Prediction")) #---> 4


# #Task4
def has_digit(lst):
    if lst.isdigit() and lst.isalpha():
        return True
    elif lst.isalpha():
        return False


print(has_digit("c8"))
print(has_digit("23cc4"))
print(has_digit("abwekz"))
print(has_digit("sdfkxi"))



#Task5
def filter_lst(shadowraze): #1 Yoli
    zxc = []
    for l in  shadowraze:
        if type(l) == int:
            zxc.append(l)
    return zxc


print(filter_lst([1, 2, 3, "a", "b", 4])) #---> [1, 2, 3, 4])

print(filter_lst(["A", 0, "Edabit", 1729, "Python", "1729"])) #---> [0, 1729])

print(filter_lst(["Nothing", "here"])) #---> []


def filter_lst1(shadowraze1): #2 Yoli
    zxc1 = []
    for l1 in shadowraze1:
        if isinstance(l1, int):
            zxc1.append(l1)
    return zxc1

print(filter_lst([1, 2, 3, "a", "b", 4])) #---> [1, 2, 3, 4])

print(filter_lst(["A", 0, "Edabit", 1729, "Python", "1729"])) #---> [0, 1729])

print(filter_lst(["Nothing", "here"])) #---> []


#Task6
def string_int(lst):
    number = int(lst)
    return number

print(string_int("6"))
print(string_int("1000"))
print(string_int("12"))



#Task7
def stutter(lst):
    return (f"{lst[0]}{lst[1]}... {lst[0]}{lst[1]}... {lst} ?")


print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))



#Task8
def name_shuffle(l):
    l = l.split()
    return f"{l[1]}, {l[0]}"

print(name_shuffle("Donald Trump"))
print(name_shuffle("Rosie O'Donnell"))
print(name_shuffle("Seymour Butts"))



#Task9
def addition(num):
    return num ++ 1

print(addition(0))
print(addition(9))
print(addition(-3))


#Task10
def is_last_character(lst):
    if 'n' in lst:
        return True
    else:
        return False


print(is_last_character("Aiden"))
print(is_last_character("Piet"))
print(is_last_character("Bert"))
print(is_last_character("Dean"))


#Task11
def return_only_integer(nevermore): #1 Yoli
    lstk = []
    for l in nevermore:
        if type(l) == int:
            lstk.append(l)
    return lstk


print(return_only_integer([9, 2, "space", "car", "lion", 16])) # ---> [9, 2, 16]
print(return_only_integer(["hello", 81, "basketball", 123, "fox"])) # ---> [81, 123]
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"])) # ---> [10, 56, 20, 3]
print(return_only_integer(["String",  True,  3.3,  1])) # ---> [1]


def return_only_integer(nevermore1): #2 Yoli
    lst = []
    for x in nevermore1:
        if isinstance(x, int):
            lst.append(x)
    return lst


print(return_only_integer([9, 2, "space", "car", "lion", 16])) # ---> [9, 2, 16]
print(return_only_integer(["hello", 81, "basketball", 123, "fox"])) # ---> [81, 123]
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"])) # ---> [10, 56, 20, 3]
print(return_only_integer(["String",  True,  3.3,  1])) # ---> [True, 1]


#Task12
def add_indexes(lst):
    lstk = []
    for x in range(len(lst)):
        lstk.append(x + lst[x])
    return lstk


print(add_indexes([0,0,0,0,0])) # ---> [0, 1, 2, 3, 4]
print(add_indexes([1,2,3,4,5])) # ---> [1, 3, 5, 7, 9]
print(add_indexes([5,4,3,2,1])) # ---> [5, 5, 5, 5, 5]



#Task13
def next_in_line(lst, num):
    if lst == []:
        return "No list has been selected"
    else:
        lst.append(num)
    return lst[1:]


print(next_in_line([5, 6, 7, 8, 9], 1)) # ---> [6, 7, 8, 9, 1]
print(next_in_line([7, 6, 3, 23, 17], 10)) # ---> [6, 3, 23, 17, 10]
print(next_in_line([1, 10, 20, 42], 6)) # ---> [10, 20, 42, 6]
print(next_in_line([], 6)) # ---> "No list has been selected"



#Task14
def society_name(list):
    zxc = []
    for x in list:
        zxc.append(x[0])
    return sorted(list)


print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))




#Task15
def halloween(zxc):
    if "10/31" in zxc:
        return "Bonfire toffee"
    else:
        return "toffee"


print(halloween("2013/10/31"))
print(halloween("2012/07/31"))
print(halloween("2011/10/12"))