def act_choose(x,y):
	calo = y;
	switcher={
    	1: calo*1.2,
  	2:calo*1.375,
   	3:calo*1.55,
   	4:calo*1.725,
   	5:calo*1.9
	 	}
	vall=switcher.get(x);
	return vall;
    
def bmr():
    weight=float(input("Enter the weight in kg:"));
    height=float(input("Enter the height in cm"));
    age=float(input("Enter the age:"));
    print("1.MALE, 2.FEMALE");
    gender=int(input("Choose your gender"));
    
        
    if gender == 1:
        cal = float()
        cal = 88.362 + (13.397*float(weight)) + (4.799*float(height)) - (5.677*float(age))
    elif gender == 2:
        cal = float()
        cal = 447.593 + (9.247*float(weight)) + (3.098*float(height)) - (4.330*float(age))

     
    print("1.Sedentary (little or no exercise),2.Lightly active (1-3 days/week),3.Moderately active (3-5 days/week,4.Very active (6-7 days/week),5.Super active (twice/day)");        
    a = int(input("Choose your act:"));

    cal = act_choose(a,cal);
    
    print("Your BMR :",cal);
bmr();



