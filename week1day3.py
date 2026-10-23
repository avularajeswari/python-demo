import numpy as np
marks=np.array([[70,80,90],
               [60, 75, 85],
               [88, 92, 79],
               [55, 65, 70]])
print("shape:", marks.shape)
print("dtype:",marks.dtype)
print("size:",marks.size)
print(marks[:2,-1])# first  two rows and last subject
student_avg=np.mean(marks,axis=1)
print("student_avg:" ,student_avg)
subject_avg=np.mean(marks,axis=0)
print("subject_avg:",subject_avg)
print("Boardcast:",marks+5)#boardcast
weights=np.array([0.3,0.3,0.4])
print("weightedscore:", np.dot(marks,weights))#dots
#reshape
reshaped_arr=np.arange(12).reshape(3,4)
print(reshaped_arr)

