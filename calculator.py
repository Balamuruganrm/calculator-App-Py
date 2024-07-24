def calculator():
        while(True):
            
                a=int(input("Enter First Number : \t\n"))
                b=int(input("Enter Second number : \n "))
                print("Please select your choice\nPRESS\n1.ADDITION\n\n2.SUBTRACTION\n\n3.MULTIPLICATION\n\n4.DIVITION\n\n5.MODULO DIVITION\n6.EXIT\n")
                ch=int(input("Please enter your choice : \t"))
                if(ch==1):
                    d=a+b
                    print("The added value is = \t",d)
                    
                elif(ch==2):
                    d=a-b
                    print("The Subtracted value is = \t",d)
                elif(ch==3):
                    d=a*b
                    print("The Multiplied value is = \t",d)
                elif(ch==4):
                    d=a/b
                    print("The Divided value is = \t",d)
                elif(ch==5):
                    d=a%b
                    print("The Remainder value is = \t",d)
                elif(ch==6):
                    print("Thank You!")
                    break
                
                else:
                    print("Your entered option is invalid! please enter the valid option")

        print("-----------Thank you!!!-----------")
calculator()
