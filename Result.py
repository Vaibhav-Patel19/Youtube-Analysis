
probability = 1;

chars = int(input("Enter number of characters in your Title (At max 100) : "))

if(chars < 10):
    probability = 0
elif(chars <= 20):
    probability = probability * (22/872)
elif(chars <= 30):
    probability = probability * (84/872)
elif(chars <= 40):
    probability = probability * (116/872)
elif(chars <= 50):
    probability = probability * (127/872)
elif(chars <= 60):
    probability = probability * (106/872)
elif(chars <= 70):
    probability = probability * (78/872)
elif(chars <= 80):
    probability = probability * (81/872)
elif(chars <= 90):
    probability = probability * (110/872)
elif(chars <= 100):
    probability = probability * (148/872)

tags = int(input("Enter number of tags in your Video(At max 100) : "))

if(tags < 10):
    probability = probability * (37/872)
elif(tags <= 20):
    probability = probability * (86/872)
elif(tags <= 30):
    probability = probability * (74/872)
elif(tags <= 40):
    probability = probability * (112/872)
elif(tags <= 50):
    probability = probability * (131/872)
elif(tags <= 60):
    probability = probability * (147/872)
elif(tags <= 70):
    probability = probability * (177/872)
elif(tags <= 80):
    probability = probability * (80/872)
elif(tags <= 90):
    probability = probability * (18/872)
elif(tags <= 100):
    probability = probability * (1/872)


day = input("Enter your day of Uploading Video : ")

if(day == "Sunday" or day == "sunday"):
    probability = probability * (74/872)
elif(day == "Monday" or day == "monday"):
    probability = probability * (103/872)
elif(day == "Tuesday" or day == "tuesday"):
    probability = probability * (154/872)
elif(day == "Wednesday" or day == "wednesday"):
    probability = probability * (147/872)
elif(day == "Thursday" or day == "thursday"):
    probability = probability * (144/872)
elif(day == "Friday" or day == "friday"):
    probability = probability * (148/872)
elif(day == "Saturday" or day == "saturday"):
    probability = probability * (102/872)


time = int(input("Enter time of uploading video in (24hr HH MM) format : "))

if(time <= 6):
    probability = probability * (235/872)
elif(time <= 12):
    probability = probability * (276/872)
elif(time <= 18):
    probability = probability * (296/872)
else:
    probability = probability * (61/872)



print(probability * 1000)


