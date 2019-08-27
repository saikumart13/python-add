def check(b):
    num_count,alp_count,lis_count = [0,0,0]
    for el in b:
       temp = el
       if(el[0].isdigit()== True):
           num_count += 1
       elif(el[0].isprintable()== True):
           alp_count += 1
       elif(type(el[0])== list):
           lis_count += 1
       else:
           None
       # if(temp.isdigit()== True):
       #     num_count += 1
       # elif(temp.isalpha()== True):
       #     alp_count += 1
       # elif(type(temp)==list):
       #     lis_count += 1
       # else:
       #     None
    if(alp_count == len(b)):
        return ''
    elif(num_count == len(b)):
        return 0
    elif(lis_count == len(b)):
        return []
    else:
        return -1

def add(a):
    sum = check(a)
    if sum == -1:
        return print("Given inputs are of different types.")
    elif sum == 0:
        for var in a:
            sum += int(var[0])
    else:
        for var in a:
            sum += var[0]
    print(sum)

#add('gh','hh')
elem = [[x] for x in input('Enter elements to be added:').split()]
add(elem)
