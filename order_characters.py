import itertools

file_to_concat = input('Please enter .txt file: ')

with open(file_to_concat) as f:
    content = f.readlines()

content = [x.strip() for x in content]

# removing duplicates
content = list(dict.fromkeys(content))

password = ""
before = [] #simply a list containing all the characters that are before any other character
# the very last character should not be in this list
after = [] # list of lists, where each list will contain [0] -> the preceding element [1] the succeeding element
prelimafter = [] #simply containing a list of all characters that are after any other character
# the very first character of the password should not be in this list

for bit in content:
    before.append(bit[0])
    prelimafter.append(bit[1])
    prelimafter.append(bit[2])
    after.append([bit[0], bit[1]])
    after.append([bit[0], bit[2]])
    after.append([bit[1], bit[2]])

# removing duplicates in list
before = list(dict.fromkeys(before))
prelimafter = list(dict.fromkeys(prelimafter))
after.sort()
list(after for after,_ in itertools.groupby(after))

potential_next = []
# for finding the very beginning in the list 
for i in before:
    if i not in prelimafter: # since the first element should not be in the after list, this will enable
        # us to get the first character
        password = password + i
        for j in after:
            if j[0] == i:
                # getting the characters that succeed the first password character
                potential_next.append(j[1])
                potential_next = list(dict.fromkeys(potential_next))
        before.remove(i)
        break

while True:
    # in this part, we are finding the next character that appears
    # in the password

    # we will go through all the characters of potential next
    new_next = potential_next[0]
    for next_car in potential_next:
        i = 0
        # going through the after list to check if there is any other character
        # that precedes new_next, that isn't already in the list
        while i < len(after) -1:
            if after[i][1] == new_next:
                if after[i][0] not in password:
                    new_next = after[i][0]
                    # if we found a character that precedes the current new_next
                    # we will restart our check to see if there is another
                    # character in after that precedes the current new_next

                    # setting i = -1 (to circumvent i += 1, the next statement)
                    # if we set i = 0, the next statement will mean we do not 
                    # check  after[0]
                    i = -1
            i += 1
    # by reaching this point, we have found the next char
    password = password + new_next
    for j in after:
        if j[0] == new_next:
            potential_next.append(j[1])
            potential_next = list(dict.fromkeys(potential_next))
    
    for j in potential_next:
        if j in password:
            potential_next.remove(j)
    #print(password)

    if potential_next == []:
        break


print(password)

