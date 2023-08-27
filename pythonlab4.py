class insurance_mng:
    insurance_type="nil"
    def __init__(self, n,a,g,con,ad):

        self.name1=n
        self.age=a
        self.gender=g
        self.contact=con
        self.ad_no=ad
    def know_your_insurance(self):
        if(self.insurance_type=="nil"):
            print("You have not subcribed to any insurance")
        else:
            print("nsurance subscribed is :",self.insurance_type)
    def get_insurance(self):
        get=(int (input("which type of insurance you want \n:"
              "1:bike\n"
              "2:car\n"
              "3:trave\n"
              "4:health\n")))
        if(get==1):
            self.insurance_type="BIKE"
        elif(get==2):
            self.insurance_type="CAR"
            print("you have successfully insured  for your car")
        elif(get==3):
            self.insurance_type="TRAVEL"
            print("you have  successfully insured for your Travelling ")

        elif(get==4):
            self.insurance_type="HEALTH"
            print("you have successfully insured for your HEALTH")
        else:
            print("please select the above options only")

    def printdetials(self):
        print("USER DETAILS")
        print(" name is :",self.name1)
        print(" age     :",self.age)
        print(" contact :",self.contact)
        print("gender   :",self.gender)
        print("aadhar   :",self.ad_no)
        print("type     :",self.insurance_type)



class child(insurance_mng):
        def insurance_package(self):
            if(self.insurance_type=="BIKE"):
                print("amount : RS 2000")
            elif(self.insurance_type=="CAR"):
                print("amount : RS 6000")
            elif(self.insurance_type=="TRAVEL"):
                print("amount : RS 10000")
            elif(self.insurance_type=="HEALTH"):
                print("amount : RS 3000")
            else:print("you have not insured anything")

        def printdetials(self, rate):
            print("USER DETAILS")
            print(" name is :", self.name1)
            print(" age     :", self.age)
            print(" contact :", self.contact)
            print("gender   :", self.gender)
            print("aadhar   :", self.ad_no)
            print("type     :", self.insurance_type)
            print("The user rating is :", rate)

student1=child("xyz",21,"male",888212321,123445671289)
student1.printdetials(6)
student2=child("yyyy",22,"female",876541221,1234456712)
student2.know_your_insurance()
student2.get_insurance()
student2.know_your_insurance()
student2.insurance_package()
