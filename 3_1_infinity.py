# Scalar UChar To UInt
# Convert unsigned char (8 bit) to unsigned integer (32 bit)

idi = self.GetInput()
dims = idi.GetDimensions()
numTuples = dims[0]*dims[1]*dims[2]
input_arr = idi.GetPointData().GetScalars()

ido = self.GetOutput()
output_arr = vtk.vtkTypeUInt32Array()
output_arr.SetName('ImageScalar')
output_arr.SetNumberOfComponents(1)
output_arr.SetNumberOfTuples(numTuples) 

num1 = 1
num2 = 1000000000

for i in range(0, numTuples):
    if input_arr.GetValue(i) == 200: #obstacle
        output_arr.SetValue(i,num1)
    elif input_arr.GetValue(i) == 100: #floor
    	output_arr.SetValue(i,0)
    else:
        # max = 2^32 - 1 = 4294967295
        output_arr.SetValue(i,num2)
        
ido.GetPointData().SetScalars(output_arr)