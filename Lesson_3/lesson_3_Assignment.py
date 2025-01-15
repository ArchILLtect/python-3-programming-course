speed = int(input("Wind speed (mph): "))
if speed < 74 :
    print ("Wind speeds to slow for hurricane")
elif speed <= 95 :
    print ("Category 1")
elif speed <= 110 :
    print ("Category 2")
elif speed <= 130 :
    print ("Category 3")
elif speed <= 155 :
    print ("Category 4")
else:
    print ("Category 5")
