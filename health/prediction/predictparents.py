def Predicted_height(name, fatherheight, motherheight):
    try:
        if fatherheight > 0 and motherheight > 0:
            PredictedHeight = (fatherheight+motherheight)/2
        #print("%s 's predicted height: %s" % (name,PredictedHeight)) 
        return PredictedHeight
    except: 
        print("Error,Missing Values in parents' height!")

a1 = Swimmer('Kim','1987-04-01',76,178,0,68)
Predicted_height(a1.name,a1.fatherheight,a1.motherheight)
