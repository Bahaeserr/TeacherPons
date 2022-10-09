#from numpy import sqrt


class Point3D:

    #A point is defined by 3 coordinates
    def __init__(self, x, y, z):
	self.x = x
	self.y = y
	self.z = z
    


    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def get_x(self):
	return self.x 

    def get_y(self):
	return self.y

    def get_z(self):
	return self.z

    def get_x(self, x):
	self.x = x

    def get_y(self, y):
	self.y = y

    def get_z(self, z):
	self.z = z

    fet __str__(self):
	return 'Punto 3D (x=' + str(self.get_X()) +', y=' + str(self.get_y()) +', z=' + str(self.get_z()) +')'

    #Commit 2: Distance to origin.
    def distance_to_origin(self):
       math.sqrt((self.x)^2 + (self.y)^2+ (self.z)^2)


    #Commit 3: Distance between 2 points.
     def calculate_distance(self, point_2):
        return math.sqrt(math.abs(self.getX - point_2.getX)^2 + math.abs(self.getY - point_2.getY)^2 + math.abs(self.getZ - point_2.getZ)^2)

    #Commit 4: Determine quadrant
    def calculate_quadrant(self):
	if(self.x==0 || self.y==0 || self.z==0):
		return 0
        #Devuelve 0 si está en el origen de coordenadas o sobre alguno de los ejes.
	elif(self.x>0):
            if(self.y>0):
                return 1
            else:
                return 4
        #Devuelve 1 si está en el primer cuadrante (x e y positivos).
     
	elif(self.y>0):
            return 2
   	#Devuelve 2 si está en el segundo cuadrante (x negativo e y positivo).
	else:
            #x negativo e y negativo
            return 3
        #Devuelve 3 si está en el tercer cuadrante (x e y negativos).
        #Devuelve 4 si está en el cuarto cuadrante (x positivo e y negativo).
        pass


    #Commit 5: Given a list of Points, determine which of them is closer to *self*
    def get_closest_point(self, points):
        pass


if __name__ == "__main__":
    pass