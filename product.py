


#Apple= 120tk/kg
#Orange= 150tk/kg
#Banana= 60tk/Dozen
#Mango= 80tk/kg
#Oil= 110tk/letre

#Item (apple)

item1="Apple"
amount= int(input("Amount of Apple in kg:"))
price1= int(input("Enter the amount of Apple in per kg:"))
Apple_price= amount*price1
print ("{0} kg {1} will cost {2} Taka".format(amount,item1,Apple_price))
vat= (amount*price1*0.1) + Apple_price
print ("{0} kg {1} will cost {2} with 10% vat".format (amount,item1,vat))


#Item (Orange)

item2="Orange"
amount1= int(input("Amount of Orange in kg:"))
price2= int(input("Enter the amount of Orange in per kg:"))

Orange_price= amount1*price2
print ("{0} kg {1} will cost {2} Taka".format(amount1,item2,Orange_price))
vat1= (amount1*price2*0.05) + Orange_price
print ("{0} kg {1} will cost {2} with 5% vat".format (amount1,item2,vat1))


#Item (Banana)

item3="Banana"
amount2= int(input("Amount of Banana in Dozen:"))
price3= int(input("Enter the amount of Banana in per Dozen:"))
Banana_price= amount2*price3
print ("{0} Dozen {1} will cost {2} Taka".format(amount2,item3,Banana_price))
vat2= (amount2*price3*0.07) + Banana_price
print ("{0} Dogen {1} will cost {2} with 7% vat".format (amount2,item3,vat2))



#Item (Mango)

item4="Mango"
amount3= int(input("Amount of Mango in kg:"))
price4= int(input("Enter the amount of Mango in per kg:"))
Mango_price= amount3*price4
print ("{0} kg {1} will cost {2} Taka".format(amount3,item4,Mango_price))
vat3= (amount3*price4*0.02) + Mango_price
print ("{0} kg {1} will cost {2} with 2% vat".format (amount3,item4,vat3))



#Item (Oil)

item5="Oil"
amount4= int(input("Amount of Oil in letre:"))
price5= int(input("Enter the amount of Oil in per letre:"))
Oil_price= amount4*price5
print ("{0} letre {1} will cost {2} Taka".format(amount4,item5,Oil_price))
vat4= (amount4*price51*0.16) + Oil_price
print ("{0} letre {1} will cost {2} with 16% vat".format (amount4,item5,vat4))


total_price= (Apple_price + Orange_price + Banana_price + Mango_price + Oil_price)
print ("Amount of total_price:",total_price)

total_vat_price = ((total_price*0.15)+total_price)
print ("Amount of total_vat price:",total_vat_price)
