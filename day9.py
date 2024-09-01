print("+++++Generation Identifier+++++")
print()
print("""Which generation are you?
Answer the following question to find out!""")
print()
year = int(input("Which year were you born?"))
if year >= 1883 and year <= 1900 :
   print ("Hello Lost Generation")  
elif year >= 1901 and year <= 1927 :
     print ("Hi Greatest Generation, Thank you for your service, sacrifice and strength.")
elif year >= 1928 and year <= 1945 :
     print ("Hello Silent Generation, Your wisdom and expirence inspire us.")
elif year >= 1946 and year <= 1964 :
     print ("Hello Baby Boomers, You are the drivers of scocial change.")
elif year >= 1965 and year <= 1980 :
     print ("Hello Generation X, You're the foundation of morden society.")
elif year >= 1981 and year <= 1996 :
     print ("Hello Millennials, Your passion and energy are contagious.")
elif year >= 1997 and year <= 2012 :
     print ("Hello Generation Z, Your creativity and innovation will shape the world.")
elif year >= 2013 :
     print ("Hello Generation Alpha, Grow, learn, thrive!")
else:
     print ("try again")