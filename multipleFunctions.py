class multiplefunction():
    def Sub_Field():
        print("Sub-Fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")

    def Eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if (Age>21):
            print("Eligible")
            message="Eligible"
        else:
            print("Not Eligible")
            message="Not Eligible"
        return message

    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total :",Total)
        print("Percentage :",(Total/5))
        percentage=Total/5
        return percentage

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area=(Height*Breadth)/2
        print("Area: (Height*Breadth)/2")
        print("Area of Traingle:",Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter=Height1+Height2+Breadth
        print("Perimeter Formula: Height1+Height2+Breadth")
        print("Perimeter of Traingle:",Perimeter)