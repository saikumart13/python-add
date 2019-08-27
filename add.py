def check(*b):
    num_count,alp_count = [0,0]
    for el in b:
       temp = str(el)
       if(temp.isdigit()== True):
           num_count += 1
       elif(temp.isalpha()== True):
           alp_count += 1
       else:
           None
    if(num_count == 0 and alp_count == len(b)):
        return ''
    elif(alp_count == 0 and num_count == len(b)):
        return 0
    else:
        return -1

def add(*a):
    sum = check(*a)
    if sum == -1:
        return print("Given inputs are of different types.")
    elif sum == 0:
        for var in a:
            sum += int(var)
    else:
        for var in a:
            sum += var
    print(sum)

#add('gh','hh')
*elem = tuple(input('Enter elements to be added:').split())
add(elem)
