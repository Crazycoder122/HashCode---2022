def parseInput(filename : str) -> list:
    with open('ip.txt') as fp:
        content = fp.read()

    content = content.split('\n')
    return content[1:]




def getAllItems(a : list) -> list:
    ans = []

    for i in a:
        for j,k in enumerate(i.split(' ')):
            if(j == 0):
                continue
            if(k not in ans):
                ans.append(k)

    return ans



def createClientChoiceGenome(like : list,dislike : list,itemsList : list) -> list:
    ans = [-1] * len(itemsList)

    for i in range(len(itemsList)):
        if(itemsList[i] in like):
            ans[i] = 1
        elif(itemsList[i] in dislike):
            ans[i] = 0
        else:
            continue

    return ans





def getClientsChoice(filename : str) -> list:
    ip = parseInput(filename)
    items = getAllItems(ip)

    ans = []

    for i in range(0,len(ip) - 1,2):
        ans.append(createClientChoiceGenome(like = ip[i].split(' ')[1:],dislike = ip[i+1].split(' ')[1:],itemsList = items))

    
    return ans