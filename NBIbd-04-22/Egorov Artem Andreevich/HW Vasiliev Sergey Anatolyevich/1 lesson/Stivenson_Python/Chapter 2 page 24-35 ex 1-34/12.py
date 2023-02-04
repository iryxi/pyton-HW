#NBIbd-04-22 Egorov Artem Andreevich
import math
def distance_calc(t1, g1, t2, g2):
    t1, g1, t2, g2 = math.radians(t1), math.radians(g1), math.radians(t2), math.radians(g2)
    distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
    return distance
t1 = float(input("Enter the latitude of first point in degrees: "))
g1 = float(input("Enter the longitude of first point in degrees: "))
t2 = float(input("Enter the latitude of second point in degrees: "))
g2 = float(input("Enter the longitude of second point in degrees: "))
result = distance_calc(t1, g1, t2, g2)
print("The distance between the points is: ", result, "km")
