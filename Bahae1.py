from math import *

class Point3D:

#A point is defined by 3 coordinates
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

#Commit 1: __init__(constructor), setters, getters and __str__ (tostring)

    def get_X(self):
        return self.x
    
    def get_Y(self):
        return self.y
    
    def get_Z(self):
        return self.z

    def set_X(self,x):
        self.x=x
    
    def set_Y(self,y):
        self.y=y

    def set_Z(self,z):
        self.z=z

    def __str__(self):
        return "X:"+str(self.x)+" Y:"+str(self.y)+" Z:"+str(self.z)

#Commit 2: Distance to origin.
  def distance_to_origin(self):

#Commit 3: Distance between 2 points.
 def calculate_distance(self, point_2):

#Commit 4: Determine quadrant
    def calculate_quadrant(self):

#Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass