# define navigable space from distance image

# May 2017 May


# Convert unsigned char scalar to unsigned short scalar
idi = self.GetInput()
dims = idi.GetDimensions()
numTuples = dims[0]*dims[1]*dims[2]
input_arr = idi.GetPointData().GetScalars()

ido = self.GetOutput()

output_arr = vtk.vtkTypeUInt32Array()
output_arr.SetName('Scalar')
output_arr.SetNumberOfComponents(1)
output_arr.SetNumberOfTuples(numTuples) 

for i in range(0, numTuples):
    val = input_arr.GetValue(i)
    if val == 10000 or val==999999900 or val==1000000000: #obstacle & outdoor space
        output_arr.SetValue(i, 0)  #non-navigable space
    else:
        output_arr.SetValue(i, 1)  #navigable space

ido.GetPointData().SetScalars(output_arr)