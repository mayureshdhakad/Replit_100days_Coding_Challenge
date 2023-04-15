mybill = float(input ("Total Bill amount? "))
tip = float(input("What percentage you want to tip?: "))
tipamount = ((tip/100)*mybill)
totalbill= mybill+ tipamount
people = int(input("How many people in your group? "))
Country = totalbill / people 
Country =round(Country,2)
print("Each person will countribute",Country)
             
            
               