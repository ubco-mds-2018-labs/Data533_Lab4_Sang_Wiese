def Predicted_height(name, fatherheight, motherheight):
    try:
        if fatherheight > 0 and motherheight > 0:
            PredictedHeight = (fatherheight+motherheight)/2
        #print("%s 's predicted height: %s" % (name,PredictedHeight)) 
        return PredictedHeight
    except: 
        print("Error,Missing Values in parents' height!")


