#Scenario: GPS Coordinates Tracker
#A delivery drone tracks its location using a simple tuple containing (latitude, longitude). You need to read and unpack these coordinates.
#Goal: Create a tuple, look up data inside it using indexes, and unpack it into separate variables.
#Your Mission
#You are tracking coordinates for a drone delivery app.
#Store a latitude of 34.0522 and a longitude of -118.2437 inside a single tuple named destination.
#First, print out the latitude by accessing index 0 of your tuple.
#Second, unpack the tuple directly into two new variables named latitude and longitude, then print them.


destination = (34.0522, -118.2437)

# Reading one value by its position. Index 0 is the first item, the latitude.
print(destination[0])

# Unpacking assigns both items at once, in order, to the names on the left.
# There have to be exactly as many names as there are items in the tuple.
latitude, longitude = destination

print(latitude)
print(longitude)
