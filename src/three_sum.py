'''
Problem statement:
Given N distinct integers, how many triples sum to exactly zero?
Plot problem - using brute force to solve

@author luzC
'''
import random
from datetime import datetime
#from datetime import timedelta


class THREESUM:

    def count(self, a):
        N = len(a)
        count = 0
        start = datetime.now()

        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if int(a[i]) + int(a[j]) + int(a[k]) == 0:
                        print("Nums: {0}, {1}, {2}".format( a[i], a[j], a[k]))
                        count +=1

        print("Elapsed time {0}".format(datetime.now() - start))
        return count

    def generate_file(self, n=100, file_name='random_number.txt'):
        print("Generating file {0}. With {1} numbers".format(file_name, n))
        with open(file_name, 'w+') as f:
            for x in range(n):
                f.write(str(random.randint(-30000,30000)) + ' ')
        return file_name

    def read_file(self, file_name):
        # Read array from file 
        print("Reading numbers from file {0}.".format(file_name))
        content = None
        with open(file_name, 'r') as f:
            content = f.readlines()
        return content[0].strip().split(' ')

# Analysis
# O(n^3)
# Able to solve problem with thousands N numbers
# We should look for billion N numbers
