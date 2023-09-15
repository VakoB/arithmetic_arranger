def arithmetic_arranger(lst: list, TorF: bool):
    hashmap = dict()
    count = -1
    if TorF == True:
        for string  in lst:
            lst2 = string.split()
            frst = lst2[0]
            opper = lst2[1]
            scnd = lst2[2]
            answ = 0
            lengthfirst = len(frst)
            lengthsecond = len(scnd)

            if lengthfirst > 4 or lengthsecond > 4:
                print('Error: Numbers cannot be more than four digits.')
                break
            if opper == '*' and opper != '/':
                print("Error: Operator must be '+' or '-'.")
                print(opper)
                break
            if len(lst) > 5:
                print('Error: Too many problems.')
                break
            if frst.isdigit() == False or scnd.isdigit() == False:
                print('Error: Numbers must only contain digits.')
                break
            
            if opper == '+':
                answ = str(int(frst) + int(scnd))
            elif opper == '-':
                answ = str(int(frst) - int(scnd))
            #second
            if lengthfirst - lengthsecond == 3:
                second = '   ' + scnd
                first = frst
            elif lengthfirst - lengthsecond == 2:
                second = '  ' + scnd
                first = frst
            elif lengthfirst - lengthsecond == 1:
                second = ' ' + scnd
                first = frst
            elif lengthfirst - lengthsecond == 0:
                second = scnd
                first = frst
            #first
            elif lengthfirst - lengthsecond == -1:
                first = ' ' + frst
                second = scnd
            elif lengthfirst - lengthsecond == -2:
                first = '  ' + frst
                second = scnd
            elif lengthfirst - lengthsecond == -3:
                first = '   ' + frst
                second = scnd
            #lines
            len_max = len(str(max(int(first),int(second))))
            if len_max == 1:
                lines = '---'
            if len_max == 2:
                lines = '----'
            if len_max == 3:
                lines = '-----'
            if len_max == 4:
                lines = '------'
            #answer
            if len(lines) - len(answ) == 1:
                answer = ' ' + answ
            if len(lines) - len(answ) == 2:
                answer = '  ' + answ
            if len(lines) - len(answ) == 3:
                answer = '   ' + answ
            if len(lines) - len(answ) == 4:
                answer = '    ' + answ
            #append every component in a list
            mList = list()
            mList.append(first)
            mList.append(opper)
            mList.append(second)
            mList.append(lines)
            mList.append(answer)
            #unique key
            count += 1
            #use dictionary
            hashmap[str(count)] = mList
        #return dictionary's values
        whitespaces = '  '
        if len(lst) == 5:
            lst1 = hashmap['0']
            lst2 = hashmap['1']
            lst3 = hashmap['2']
            lst4 = hashmap['3']
            lst5 = hashmap['4']
            print(' ',lst1[0],whitespaces,' ',lst2[0],whitespaces,' ',lst3[0],whitespaces,' ',lst4[0],whitespaces,' ',lst5[0])
            print(lst1[1], lst1[2],whitespaces,lst2[1], lst2[2],whitespaces,lst3[1], lst3[2],whitespaces,lst4[1], lst4[2],whitespaces,lst5[1], lst5[2])
            print(lst1[3],whitespaces, lst2[3],whitespaces,lst3[3],whitespaces,lst4[3],whitespaces,lst5[3])
            print(lst1[4],whitespaces,lst2[4],whitespaces,lst3[4],whitespaces,lst4[4],whitespaces,lst5[4])
        if len(lst) == 4:
            lst1 = hashmap['0']
            lst2 = hashmap['1']
            lst3 = hashmap['2']
            lst4 = hashmap['3']
            print(' ',lst1[0],whitespaces,' ',lst2[0],whitespaces,' ',lst3[0],whitespaces,' ',lst4[0])
            print(lst1[1], lst1[2],whitespaces,lst2[1], lst2[2],whitespaces,lst3[1], lst3[2],whitespaces,lst4[1], lst4[2])
            print(lst1[3],whitespaces, lst2[3],whitespaces,lst3[3],whitespaces,lst4[3])
            print(lst1[4],whitespaces,lst2[4],whitespaces,lst3[4],whitespaces,lst4[4])
        elif len(lst) == 3:
            lst1 = hashmap['0']
            lst2 = hashmap['1']
            lst3 = hashmap['2']
            print(' ',lst1[0],whitespaces,' ',lst2[0],whitespaces,' ',lst3[0])
            print(lst1[1], lst1[2],whitespaces,lst2[1], lst2[2],whitespaces,lst3[1], lst3[2])
            print(lst1[3],whitespaces, lst2[3],whitespaces,lst3[3])
            print(lst1[4],whitespaces,lst2[4],whitespaces,lst3[4])
        elif len(lst) == 2:
            lst1 = hashmap['0']
            lst2 = hashmap['1']
            print(' ',lst1[0],whitespaces,' ',lst2[0])
            print(lst1[1], lst1[2],whitespaces,lst2[1],lst2[2])
            print(lst1[3],whitespaces,lst2[3])
            print(lst1[4],whitespaces,lst2[4])
        elif len(lst) == 1:
            lst1 = hashmap['0']
            print(' ',lst1[0])
            print(lst1[1], lst1[2])
            print(lst1[3])
            print(lst1[4])

arithmetic_arranger(["32 + 8", "1 - 3801", "4 - 2", "1000 + 1000", "912 + 3242"], True)
