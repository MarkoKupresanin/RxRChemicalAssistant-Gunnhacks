from curses.ascii import isalpha
import json
import math




def synthesisCalculation(reactantOne, reactantTwo, product):
    if reactantOne==None or reactantTwo==None or product==None:
        return "Incomplete Equation"


    temp=[]
    temp1=[]
    temp2=[]
    temp2a=[]
    pairTuple=[]
    pairTuple2=[]
    reactantOneLayout=[]
    reactantTwoLayout=[]
    productLayout=[]

    for character in reactantOne:
        if character=="(" or character==")":
            reactantOneLayout.append("()")
        elif not isalpha(character):
            reactantOneLayout.append("N")
        elif isalpha(character):
            if character.islower():
                reactantOneLayout.append("a")
            else:
                reactantOneLayout.append("A")
        else:
            return print("Unsupported character a")
    for character in reactantTwo:
        if character=="(" or character==")":
            reactantTwoLayout.append("()")
        elif not isalpha(character):
            reactantTwoLayout.append("N")
        elif isalpha(character):
            if character.islower():
                reactantTwoLayout.append("a")
            else:
                reactantTwoLayout.append("A")
        else:
            return print("Unsupported character b")
    for character in product:
        if character=="(" or character==")":
            productLayout.append("()")
        elif not isalpha(character):
            productLayout.append("N")
        elif isalpha(character):
            if character.islower():
                productLayout.append("a")
            else:
                productLayout.append("A")
        else:
            return print("Unsupported character c")
    
    if reactantOneLayout[0]=="N":
        return print("You made an error in formatting")
    if reactantTwoLayout[0]=="N":
        return print("You made an error in formatting")
    if productLayout[0]=="N":
        return print("You made an error in formatting")

    # print(reactantOneLayout)
    # print(reactantTwoLayout)
    # print(productLayout)

    if reactantOneLayout[0]=="A" and reactantOneLayout[1]=="a":
        # temp.append(str(reactantOne[0])+str(reactantOne[1])+str(reactantOne[2]))
        temp.append(str(reactantOne[0])+str(reactantOne[1]))
    
    elif reactantOneLayout[0]=="A" and reactantOneLayout[1]=="N":
        # temp.append(str(reactantOne[0])+str(reactantOne[1]))
        temp.append(str(reactantOne[0]))
    #####
    if reactantTwoLayout[0]=="A" and reactantTwoLayout[1]=="a":
        # temp.append(str(reactantTwo[0])+str(reactantTwo[1])+str(reactantTwo[2]))
        temp1.append(str(reactantTwo[0])+str(reactantTwo[1]))
    elif reactantTwoLayout[0]=="A" and reactantTwoLayout[1]=="N":
        # temp.append(str(reactantTwo[0])+str(reactantTwo[1]))
        temp1.append(str(reactantTwo[0]))
    #####
    if productLayout[0]=="A" and productLayout[1]=="a":
        # temp2.append(str(product[0])+str(product[1])+str(product[2]))
        temp2.append(str(product[0])+str(product[1]))
    elif productLayout[0]=="A" and productLayout[1]=="N":
        # temp2.append(str(product[0])+str(product[1]))
        temp2.append(str(product[0]))
    elif productLayout[0]=="A" and productLayout[1]=="A" and productLayout[2]=="a" and productLayout[3]=="N":
        # temp2a.append(str(product[0])+str(product[1])+str(product[2])+str(product[3]))
        temp2a.append(str(product[0]))
        temp2a.append(str(product[1])+str(product[2]))

    
    # for reactant 1
    with open("PeriodicTable.json", "r") as f:
        jsonData=json.load(f)
        for i in jsonData["order"]:
            for thing in temp:
                if thing == jsonData[i]["symbol"]:
                    if reactantOneLayout[0]=="A" and reactantOneLayout[1]=="a":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple.append((thing,int(jsonData[i]["xpos"])-10, reactantOne[2]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple.append((thing,"varying", reactantOne[2]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple.append((thing,int(jsonData[i]["xpos"]), reactantOne[2]))
                    elif reactantOneLayout[0]=="A" and reactantOneLayout[1]=="N":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple.append((thing,int(jsonData[i]["xpos"])-10, reactantOne[1]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple.append((thing,"varying", reactantOne[1]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple.append((thing,int(jsonData[i]["xpos"]), reactantOne[1]))
    # for reactant 2
    with open("PeriodicTable.json", "r") as f:
        jsonData=json.load(f)
        for i in jsonData["order"]:
            for thing in temp1:
                if thing == jsonData[i]["symbol"]:
                    if reactantTwoLayout[0]=="A" and reactantTwoLayout[1]=="a":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple.append((thing,int(jsonData[i]["xpos"])-10, reactantTwo[2]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple.append((thing,"varying", reactantTwo[2]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple.append((thing,int(jsonData[i]["xpos"]), reactantTwo[2]))
                    elif reactantTwoLayout[0]=="A" and reactantTwoLayout[1]=="N":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple.append((thing,int(jsonData[i]["xpos"])-10, reactantTwo[1]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple.append((thing,"varying", reactantTwo[1]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple.append((thing,int(jsonData[i]["xpos"]), reactantTwo[1]))


    #for product   2 1 3
    with open("PeriodicTable.json", "r") as f:
        jsonData=json.load(f)
        for i in jsonData["order"]:
            for thing in temp2:
                if thing == jsonData[i]["symbol"]:
                    if productLayout[0]=="A" and productLayout[1]=="a":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple.append((thing,int(jsonData[i]["xpos"])-10, product[2]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple.append((thing,"varying", product[2]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple.append((thing,int(jsonData[i]["xpos"]), product[2]))
                    elif productLayout[0]=="A" and productLayout[1]=="N":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple.append((thing,int(jsonData[i]["xpos"])-10, product[1]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple.append((thing,"varying", product[1]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple.append((thing,int(jsonData[i]["xpos"]), product[1]))
                    elif productLayout[0]=="A" and productLayout[1]=="A" and productLayout[2]=="a" and productLayout[3]=="N":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple.append((thing,int(jsonData[i]["xpos"])-10, product[3]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple.append((thing,"varying", product[3]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple.append((thing,int(jsonData[i]["xpos"]), product[3]))

            for thing in temp2a:
                if thing == jsonData[i]["symbol"]:
                    if productLayout[0]=="A" and productLayout[1]=="a":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple2.append((thing,int(jsonData[i]["xpos"])-10, product[2]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple2.append((thing,"varying", product[2]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple2.append((thing,int(jsonData[i]["xpos"]), product[2]))
                    elif productLayout[0]=="A" and productLayout[1]=="N":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple2.append((thing,int(jsonData[i]["xpos"])-10, product[1]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple2.append((thing,"varying", product[1]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple2.append((thing,int(jsonData[i]["xpos"]), product[1]))
                    elif productLayout[0]=="A" and productLayout[1]=="A" and productLayout[2]=="a" and productLayout[3]=="N":
                        if int(jsonData[i]["xpos"])>=13:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"])-10)
                            pairTuple2.append((thing,int(jsonData[i]["xpos"])-10, product[3]))
                        elif int(jsonData[i]["xpos"])>=3 and int(jsonData[i]["xpos"])<=12:
                            #print(thing,jsonData[i]["name"],"Varying charge")
                            pairTuple2.append((thing,"varying", product[3]))
                        else:
                            #print(thing,jsonData[i]["name"],int(jsonData[i]["xpos"]))
                            pairTuple2.append((thing,int(jsonData[i]["xpos"]), product[3]))


    #if AN AaN AAaN
    if productLayout[0]=="A" and productLayout[1]=="A" and productLayout[2]=="a" and productLayout[3]=="N":
        lhs1=int(pairTuple[0][2])
        lhs2=int(pairTuple[1][2])
        rhs1=1
        rhs2=int(pairTuple2[1][2])

        if lhs1==rhs1:
            print("These are all good")
        else:
            rhs1=lhs1*rhs1
            rhs2=lhs1*rhs2
        if lhs2==rhs2:
            print("also good ")
        else:
            while lhs2!=rhs2:
                for i in range(101):
                    lhs2*i
            
            print(lhs1)
            print(lhs2)
            print(rhs1)
            print(rhs2)            

        # coefficientOne=
        # coefficientTwo=
        # coefficientThree=rhs1
        

    print(lhs1)
    print(lhs2)
    print(rhs1)
    print(rhs2)



    # with open("PeriodicTable.json", "r") as f:
    #     jsonData=json.load(f)
    #     for i in jsonData["order"]:
    #         for thing in temp:
    #             if thing == jsonData[i]["symbol"]:
    #                 print(thing,jsonData[i]["name"])

    # print(temp)
    # print(temp2)
    # print(temp2a)
    print(pairTuple)
    print(pairTuple2)
# [('P', 5, '4'), ('Br', 7, '2')]
# [('P', 5, '3'), ('Br', 7, '3')]

    return "Complete"

synthesisCalculation("P4", "Br2", "PBr3")