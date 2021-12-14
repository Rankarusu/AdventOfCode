#please forgive me whoever reads this. 

def get_diff(eight:str, nine:str):
    for x in eight:
        if x not in nine:
            return x

def sort_string(string:str):
    return "".join(sorted(string))

def get_digits(input):
    dic = {"1":"", "2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":""}

    inputstream = input.split()
    for x in inputstream:
        if len(x) == 2:
            dic["1"] = sort_string(x)
        elif len(x) == 3:
            dic["7"] = sort_string(x)
        elif len(x) == 4:
            dic["4"] = sort_string(x)
        elif len(x) == 7:
            dic["8"] = sort_string(x)

        
    for x in inputstream:
        if len(x) == 6:
            if set(dic["4"]).issubset(x):
                dic["9"] = sort_string(x) # 9 contains all segements of 4
            elif set(dic["1"]).issubset(x):
                dic["0"] = sort_string(x)
            else:
                dic["6"] = sort_string(x)
 
    bottom_left = get_diff(dic["8"], dic["9"])
    
    for x in inputstream:
        if len(x) == 5:
            if set(dic["1"]).issubset(x):
                dic["3"] = sort_string(x)
            elif bottom_left in x:
                dic["2"] = sort_string(x)
            else:
                dic["5"] = sort_string(x)

    return dict((v,k) for k,v in dic.items())   #flip the dictionary as we need to search the other way round this time. probabably a horrible solution

def get_num(dic:dict, string:str):
    return dic.get(string)


with open("08-input.txt") as file:
    lines = file.readlines()
    lines = [x.strip() for x in lines]
    sum = 0

    for line in lines:
        seg, num = line.split("|")
        decoder = get_digits(seg)
        output = ""
        for x in num.split():
            strx = sort_string(x)
            output += str(get_num(decoder, strx))
        print(output)
        sum += int(output)

print(sum)