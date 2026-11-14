import random
l=[1,2,3,4,5,6,7,8,9,10]
yt=["batting","bawling"]
def batting():
    print("Now My Bawling , Your Batting")
    print("")
    o=0
    while True:
        c= random.choice(l)
        u= int(input("Play Batting --"))
        print(c)
        o=o+u
        if u==c:
            print("OUT !!")
            print("Your Total Run --",o)
            print("Now My Batting , Your Bawling")
            print("")
            k=0
            while True:
                us=int(input("Play Bawling --"))
                cc= random.choice(l)
                print(cc)
                k=k+cc
                if k>o:
                    print("!!")
                    print("My Total Run --",k)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    print("")
                    print("I Won The Game")
                    
                    return
                elif cc==us:
                    print("OUT !!")
                    print("My Total Run --",k)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    print("")
                    if o>k:
                        print("You Won The Game")
                        
                        return
                        
                    elif o<k:
                        print("I Won The Game")
                        
                        return
                    else:
                        print("Tie")
                        
                        return
                
def bawling():
    print("Now My Batting , Your Bawling")
    print("")
    k=0
    while True:
        us=int(input("Play Bawling --"))
        cc= random.choice(l)
        print(cc)
        k=k+cc
        if cc==us:
            print("OUT !!")
            print("My Total Run --",k)
            print("Now My Bawling , Your Batting")
            print("")
            o=0
            while True:
                c= random.choice(l)
                u= int(input("Play Batting --"))
                print(c)
                o=o+u
                if o>k:
                    print("Out !!")
                    print("Your Total Run --",o)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    print("")
                    print("You Won The Game")
                    
                    return
                elif u==c:
                    print("OUT !!")
                    print("Your Total Run --",o)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    print("")
                    if o>k:
                        print("You Won The Game")
                        
                        return
                        
                    elif o<k:
                        print("I Won The Game")
                        
                        return
                    else:
                        print("Tie")
                        
                        return
def crazybatting():
    print("Now My Bawling , Your Batting")
    print("")
    o=0
    while True:
        c= random.choice(l)
        u= int(input("Play Batting --"))
        print(c)
        if u==c:
            u=(u**2)
            
            print("")
        o=o+u
        if c==(u-1) or c==(u+1) or (c==10 and u==1) or (u==10 and c==1):
            print("OUT !!")
            print("Your Total Run --",o)
            print("Now My Batting , Your Bawling")
            print("")
            k=0
            while True:
                us=int(input("Play Bawling --"))
                cc= random.choice(l)
                print(cc)
                if us==cc:
                    cc=(cc**2)
                    
                    print("")
                k=k+cc
                if k>o:
                    print("Out !!")
                    print("My Total Run --",k)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    print("")
                    print("I Won The Game")
                    
                    return
                if us==(cc-1) or us==(cc+1) or (cc==10 and us==1) or (us==10 and cc==1):
                    print("OUT !!")
                    print("My Total Run --",k)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    print("")
                    if o>k:
                        print("You Won The Game")
                        
                        return
                        
                    elif o<k:
                        print("I Won The Game")
                        
                        return
                    else:
                        print("Tie")
                        
                        return
def crazybawling():
    print("Now My Batting , Your Bawling")
    print("")
    k=0
    while True:
        us=int(input("Play Bawling --"))
        cc= random.choice(l)
        print(cc)
        if us==cc:
            cc=(cc**2)
            
            print("")
        k=k+cc
        if us==(cc+1) or us==(cc-1) or (cc==10 and us==1) or (us==10 and cc==1):
            print("OUT !!")
            print("My Total Run --",k)
            print("Now My Bawling , Your Batting")
            print("")
            o=0
            while True:
                c= random.choice(l)
                u= int(input("Play Batting --"))
                print(c)
                if u==c:
                    u=(u**2)
                    
                    print("")
                o=o+u
                if o>k:
                    print(" !!")
                    print("Your Total Run --",o)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    print("")
                    print("You Won The Game")
                    
                    return
                if c==(u-1) or c==(u+1) or (c==10 and u==1) or (c==1 and u==10):
                    print("OUT !!")
                    print("Your Total Run --",o)
                    print("")
                    print("    Score")
                    print("YOU  //  COMPUTER")
                    print("",o,"//   ",k)
                    if o>k:
                        print("You Won The Game")
                        
                        return
                    elif o<k:
                        print("I Won The Game")
                        
                        return
                    else:
                        print("Tie")
                        
                        return
while True:
    p=input("Normal OR Crazy --").lower()
    q=["normal","crazy"]
    if p not in q:
        
        print("Are you sure, You want to Exit ")
        b=input("(y/n)").lower()
        if b=="y":
            break
        elif b=="n":
            continue
        else:
            print("Invalid input :\\ ")
            break
    if p=="normal":
        z=input("Choose (Odd/Even)").lower()
        if z =="odd":
            x=int(input("Play --"))
            e=random.choice(l)
            vs=x+e
            print(e)
            if vs%2==0:
                print(vs,"Its Even")
                rt=random.choice(yt)
                if rt =="bawling":
                    batting()
                    break
                else:
                    bawling()
                    break
            else:
                print(vs,"Its Odd")
                rt=input("Batting/Bawling --").lower()
                if rt =="batting":
                    batting()
                    break
                else:
                    bawling()
                    break
        elif z =="even":
            x=int(input("Play --"))
            e=random.choice(l)
            vs=x+e
            print(e)
            if vs%2==0:
                print(vs,"Its Even")
                rt=input("Batting/Bawling --").lower()
                if rt =="batting":
                    batting()
                    break
                else:
                    bawling()
                    break
            else:
                print(vs,"Its Odd")
                rt=random.choice(yt)
                if rt =="bawling":
                    batting()
                    break
                else:
                    bawling()
                    break
    elif p=="crazy":
        z=input("Choose (Odd/Even)").lower()
        if z =="odd":
            x=int(input("Play --"))
            e=random.choice(l)
            vs=x+e
            print(e)
            if vs%2==0:
                print(vs,"Its Even")
                rt=random.choice(yt)
                if rt =="bawling":
                    crazybatting()
                    break
                elif rt=="batting":
                    crazybawling()
                    break
            else:
                print(vs,"Its Odd")
                rt=input("Batting/Bawling --").lower()
                if rt =="batting":
                    crazybatting()
                    break
                elif rt=="bawling":
                    crazybawling()
                    break
        elif z =="even":
            x=int(input("Play --"))
            e=random.choice(l)
            vs=x+e
            print(e)
            if vs%2==0:
                print(vs,"Its Even")
                rt=input("Batting/Bawling --").lower()
                if rt =="batting":
                    crazybatting()
                    break
                elif rt=="bawling":
                    crazybawling()
                    break
            else:
                print(vs,"Its Odd")
                rt=random.choice(yt)
                if rt =="bawling":
                    crazybatting()
                    break
                elif rt=="batting":
                    crazybawling()
                    break
print("")
print("Thanks For Playing")










