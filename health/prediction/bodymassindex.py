def bmi(name, height, weight):
        height = height/100 #Convert cm to meters
        BMI = weight/(height*height)
        return BMI
        #print("%s BMI is: %s" % (name,BMI))
        #if BMI < 18.5:
        #    print (name,"is underweight. Please eat more along with exercises!")
        #elif BMI >= 18.5 and BMI <= 24.9:
        #    print (name,"is at normal weight. Keep up with the good work!")
        #elif BMI >= 25 and BMI <= 29.9:
        #    print (name,"is overweight. Please work out more and eat more healthy!")
        #elif BMI >= 30:
        #    print (name,"is a bit obese. Please work out more and eat more healthy!!!")
