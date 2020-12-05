
import os
import numpy as np 


def get_values(array):
	sum=2020
	array=np.sort(array)
	ind=0
	for val in array:
		tmp_arr=np.delete(array, ind)
		ind+=1
		search_val=sum-val
		if search_val in tmp_arr:
			print("********")
			print(search_val*val)
			break

def find_triplet(A, arr_size):
	sum=2020
	for i in range(0, arr_size-1):
		s=set()
		search_val=sum-A[i]
		for j in range(i+1, arr_size):
			if (search_val-A[j]) in s:
				print("Solution found: ")
				print(A[i], " ", A[j], " ", search_val-A[j])
				print("The product: ",  A[i]*A[j]*(search_val-A[j]))
			s.add(A[j])







cwd = os.getcwd()
filename=cwd+"/inputs/day_1.txt"
lines = (line.rstrip() for line in open(filename))

array=np.array(list(lines), dtype=np.float32)

#print(array)
#get_values(array)
find_triplet(array, len(array))