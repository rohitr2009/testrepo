usa=["altalnta", "newoyk", "chicago", "baltimore"]
uk=["london", "bristol", "cambridge"]
india=["mumbai", "delhi", "banglore"]

city=input("enter a city name:")
if city in usa:
    print("usa")
elif city in uk:
    print("uk")
elif city in india:
    print("india")
else:
    print(city, "is out of my database")
