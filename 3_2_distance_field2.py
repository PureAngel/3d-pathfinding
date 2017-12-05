# Distance field 3D Chamfer 5x5x5
# Required input volume:
# - Object has value 0
# - Empty space has value infinity (A number greater than the maximum possible distance)

# May 2016 - Martijn Koopman

# ToDo: Clean code; pass variable dims to function GetArrValue() and SetArrValue() as arguments

# Read input
idi = self.GetInput()
dims = idi.GetDimensions()
arr = idi.GetPointData().GetScalars()

# Create output
ido = self.GetOutput()
distArr = vtk.vtkTypeUInt32Array()
distArr.DeepCopy(arr)
distArr.SetName('distance')

obstacle_num = 1

height = 100  #100cm  to the floor
# Utility functions
def GetArrValue(arr, pos):
    if pos[0] < 0 or pos[0] >= dims[0] or pos[1] < 0 or pos[1] >= dims[1] or pos[2] < 0 or pos[2] >= dims[2]:
        return 1000000000   # 0
    else:
        i = pos[0] + (pos[1] * dims[0]) + (pos[2] * dims[0] * dims[1])
        return arr.GetValue(i)

def SetArrValue(arr, pos, val):
    i = pos[0] + (pos[1] * dims[0]) + (pos[2] * dims[0] * dims[1])
    arr.SetValue(i, val)

def check(x, y, z, dx, dy, dz, v):
    #if GetArrValue(distArr,(x+dx,y+dy,z+dz)) != obstacle_num: # add
    n = GetArrValue(distArr, (x+dx, y+dy, z+dz)) + v
    if GetArrValue(distArr, (x,y,z)) >  n:
      SetArrValue(distArr, (x,y,z), n)


for z in range(dims[2]):
    for y in range(dims[1]):
        for x in range(dims[0]):            
            if GetArrValue(distArr, (x, y, z)) == 10000:
                  SetArrValue(distArr, (x, y, z), 100) # distance from the surface whose height=100
            if GetArrValue(distArr, (x, y, z)) >= 150:
                  SetArrValue(distArr, (x, y, z), 0)

                  


ido.GetPointData().SetScalars(distArr)