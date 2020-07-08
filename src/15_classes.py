# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon): 
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    # the '__str__' method allows us to defin how the class is printed out.
    def __str__(self):
        # this method treunrns a string that can be printed
        return f"<Waypoint '{self.name}', {self.lat}, {self.lon}>"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"<Geocache '{self.name}', {self.difficulty}, {self.size}, {self.lat}, {self.lon}>"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)



# Practice
import turtle

class Polygon:
    def __init__(self, sides, name, size = 100, color = "black", line_thickness=2):
        self.sides = sides
        self.name = name
        self.color = color
        self.line_thickness = line_thickness
        self.size = size
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

#     def draw(self):
#         turtle.color(self.color)
#         turtle.pensize(self.line_thickness)
#         for i in range(self.sides):
#             turtle.forward(self.size)
#             turtle.right(180-self.angle)
#         turtle.done()


# square = Polygon(4, "Square")
# pentagon = Polygon(5, "Pentegon")

# print(square.sides)
# print(square.name)
# print(square.interior_angles)
# print(square.angle)

# print(pentagon.sides)
# print(pentagon.name)

# hexagon = Polygon(6, "Hexagon", color="red", line_thickness = 40)
# hexagon.draw()

# pentagon.draw()

class Square(Polygon):
    def __init__(self, size = 100, color = "black", line_thickness=2 ):
        super().__init__(4, "Square", size, color, line_thickness)

square = Square()

print(square.sides)
print(square.angle)