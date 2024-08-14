class Assignments():
    def Subfields():
        print("Sub-fields in AI are:");
        myList = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing'];
        for x in myList:
            print(x);

    def OddEven() :
        enteredNum = int(input("Enter a number:"));
        if(enteredNum%2 !=0):
            print(enteredNum," is Odd number");
        else:
            print(enteredNum," is Even number");

    def Eligible():
        sex = input("Enter your sex (type --> Male or Female):");
        age = int(input("Enter your age:"));
        if((sex == "Male") | (sex=="male")):
            if(age<21):
                print("MALE IS NOT ELIGIBLE FOR MARRIAGE");
            else:
                print("MALE IS ELIGIBLE FOR MARRIAGE");

        if((sex == "Female") | (sex=="female")):
            if(age<18):
                print("FEMALE IS NOT ELIGIBLE FOR MARRIAGE");
            else:
                print("FEMALE IS ELIGIBLE FOR MARRIAGE");

    def percentage():
        Subject1 = int(input("Enter marks for Subject1:"));
        Subject2 = int(input("Enter marks for Subject2:"));
        Subject3 = int(input("Enter marks for Subject3:"));
        Subject4 = int(input("Enter marks for Subject4:"));
        Subject5 = int(input("Enter marks for Subject5:"));
        subjectList = [Subject1,Subject2,Subject3,Subject4,Subject5];
        Total = 0;
        for k in subjectList:
            Total += k;

        percentage = Total/len(subjectList);
        print("Total:",Total);
        print("Percentage:",percentage);

    def triangle():
        height = int(input("Enter height of the triangle:"));
        breadth = int(input("Enter breadth of the triangle:"));
        area = (height*breadth)/2;
        print("Area of Triangle:",area);
        height1 = int(input("Enter height1 of the triangle:"));
        height2 = int(input("Enter height2 of the triangle:"));
        breadth1 = int(input("Enter breadth1 of the triangle:"));
        perimeter = height1+height2+breadth1;
        print("Perimeter of Triangle:",perimeter);