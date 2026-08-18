# Register No:212225040394
# Developed By:SENASH AYISHA F
# 1-Norm of a Matrix
import os
os.environ["OPENBLAS_NUM_THREADS"]="1"
import numpy as np
matrix=np.array(eval(input()))
result=np.linalg.norm(matrix,1)
print(result)




# 2-Norm of a Matrix

import os
os.environ["OPENBLAS_NUM_THREADS"]="1"
import numpy as np 
matrix=np.array(eval(input()))
result=np.linalg.norm(matrix,2)
print("{0:.2f}".format(result))


# Infinity Norm of a Matrix

import os
os.environ["OPENBLAS_NUM_THREADS"]="1"
import numpy as np
matrix=np.array(eval(input()))

result=np.linalg.norm(matrix,np.inf)
print(result)


