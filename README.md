# Norm of a matrix
## Aim
To write a program to find the 1-norm, 2-norm and infinity norm of the matrix and display the result in two decimal places.
## Equipment’s required:
1.	Hardware – PCs
2.	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
	1. Get the input matrix using np.array()   
    2. Find the 2-norm of the matrix using np.linalg.norm()
	3. Print the norm of the matrix in two decimal places.
## Program:
```Python
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



```
## Output:
### 1-Norm of a Matrix
<img width="1016" height="908" alt="image" src="https://github.com/user-attachments/assets/1d95736d-325f-4674-8e19-7e34fac2cf83" />

<br>
<br>
<br>

### 2-Norm of a Matrix
<img width="842" height="905" alt="image" src="https://github.com/user-attachments/assets/cbad3126-b312-4294-991f-b68d3d422cd6" />

<br>
<br>
<br>

### Infinity Norm of a Matrix
<img width="971" height="901" alt="image" src="https://github.com/user-attachments/assets/0212cb91-03b5-4d74-84a4-a4c4a2899c80" />

<br>
<br>
<br>

## Result
Thus the program for 1-norm, 2-norm and Infinity norm of a matrix are written and verified.
