'''
Pc=str(input("Enter the name of Pc part whose price you want to check :- \n 1.Processor \n 2.Graphics card \n 3.Ram \n Value = "))
if Pc == '1':
    processor=input(str("Enter the model of the cpu whose price you would like to check \n 1.Intel i9 - 10900k \n 2.Ryzen 9 - 3950x \n Value = "))
    try:
        if processor==1:
            print("Price of intel i9-10900k is ₹53000")
        else:
            print("Price of Ryzen 9 - 3950x is ₹72000")
    except:
        print()

elif Pc == '2':
    try:
        graphicscard=input(str("Enter the model of the gpu whose price you would like to check \n 1.Rtx 3090 Trinity 24gb \n 2.Radeon Rx 6900 XT 16gb \n Value = "))
        if graphicscard==1:
            print("Price of Rtx 3090 is ₹2,63,000")
        else:
            print("Price of Radeon Rx 6900 XT is ₹1,74,000")
    except:
        print()
elif Pc == '3':
    try:
        ram=input(str("Enter the model of the ram whose price you would like to check \n 1.G.SKILL Trident Z RGB 16GB(2x8 GB) \n 2.G.SKILL Trident Z Neo 16GB (2x8 GB) \n Value = "))
        if ram==1:
            print("Price of G SKILL Trident Z is ₹11,500")
        else:
            print("Price of G SKILL Trident Z Neo is ₹10,500")
    except:
        print()
else:
    print("error")
    '''
'''
Pc=input("enter")
if '1' == Pc:
    processor=input(str("Enter the model of the cpu whose price you would like to check \n 1.Intel i9 - 10900k \n 2.Ryzen 9 - 3950x \n Value = "))
    if processor==1:
        print("Price of intel i9-10900k is ₹53000")
    else:
        print("Price of Ryzen 9 - 3950x is ₹72000")
elif Pc==2:
    graphicscard=input(str("Enter the model of the gpu whose price you would like to check \n 1.Rtx 3090 Trinity 24gb \n 2.Radeon Rx 6900 XT 16gb \n Value = "))
    if graphicscard==1:
        print("Price of Rtx 3090 is ₹2,63,000")
    else:
        print("Price of Radeon Rx 6900 XT is ₹1,74,000")
elif Pc==3:
    ram=input(str("Enter the model of the ram whose price you would like to check \n 1.G.SKILL Trident Z RGB 16GB(2x8 GB) \n 2.G.SKILL Trident Z Neo 16GB (2x8 GB) \n Value = "))
    if ram==1:
        print("Price of G SKILL Trident Z is ₹11,500")
    else:
        print("Price of G SKILL Trident Z Neo is ₹10,500")
else:
    print("error")
'''

Pc=input(str("Enter the name of Pc part whose price you want to check :- \n 1.Processor \n 2.Graphics card \n 3.Ram \n Value = "))
if Pc=='1':
    processor=input(str("Enter the model of the cpu whose price you would like to check \n 1.Intel i9 - 10900k \n 2.Ryzen 9 - 3950x \n Value = "))
    if processor=='1':
        print("Price of intel i9-10900k is ₹53000")
    else:
        print("Price of Ryzen 9 - 3950x is ₹72000")
elif Pc=='2':
    graphicscard=input(str("Enter the model of the gpu whose price you would like to check \n 1.Rtx 3090 Trinity 24gb \n 2.Radeon Rx 6900 XT 16gb \n Value = "))
    if graphicscard=='1':
        print("Price of Rtx 3090 is ₹2,63,000")
    else:
        print("Price of Radeon Rx 6900 XT is ₹1,74,000")
elif Pc=='3':
    ram=input(str("Enter the model of the ram whose price you would like to check \n 1.G.SKILL Trident Z RGB 16GB(2x8 GB) \n 2.G.SKILL Trident Z Neo 16GB (2x8 GB) \n Value = "))
    if ram =='1':
        print("Price of G SKILL Trident Z is ₹11,500")
    else:
        print("Price of G SKILL Trident Z Neo is ₹10,500")
else:
    print("error")
        