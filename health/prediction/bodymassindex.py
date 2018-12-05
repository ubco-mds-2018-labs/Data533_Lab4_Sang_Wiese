def bmi(name, height, weight):
        height = height/100 #Convert cm to meters
        
        try:    
            BMI = weight/(height*height)
            #print("%s BMI is: %s" % (name,BMI))
            #if BMI < 18.5:
            #    print (name,"is underweight. Please eat more along with exercises!")
            #elif BMI >= 18.5 and BMI <= 24.9:
            #    print (name,"is at normal weight. Keep up with the good work!")
            #elif BMI >= 25 and BMI <= 29.9:
            #    print (name,"is overweight. Please work out more and eat more healthy!")
            #elif BMI >= 30:
            #    print (name,"is a bit obese. Please work out more and eat more healthy!!!")
            #return BMI

        except:
            print("Error, Missing value in height or weight")
      
a1 = Swimmer('Kim','1987-04-01',0,178,75,68)
bmi(a1.name,a1.height,a1.weight)
