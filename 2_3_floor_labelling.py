# Segment ground voxels

# User defined parameter:
segment_num = 1       # Number of segment that includes floor and stairs

# Convert unsigned char scalar to unsigned short scalar
idi = self.GetInput()
dims = idi.GetDimensions()
numTuples = dims[0]*dims[1]*dims[2]
input_arr = idi.GetPointData().GetScalars()

ido = self.GetOutput()
output_arr = vtk.vtkUnsignedCharArray()
output_arr.SetName('Scalar')
output_arr.SetNumberOfComponents(1)
output_arr.SetNumberOfTuples(numTuples) 

for i in range(0, numTuples):
    val = input_arr.GetValue(i)
    if val == 0:
        output_arr.SetValue(i, 0)
    elif val == segment_num:
        output_arr.SetValue(i, 100) #floor
    elif val == 3:
        output_arr.SetValue(i, 200) #obstacle
    else:
        output_arr.SetValue(i, 200) #obstacle

ido.GetPointData().SetScalars(output_arr)