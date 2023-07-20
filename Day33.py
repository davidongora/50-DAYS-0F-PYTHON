list1 = [10, 20 ,30]
list2 = [10, 110 ,30]
def inter_section(a, b):
    inter_list = tuple([i for i in a if i in b]) 
    return inter_list
print(inter_section(list1, list2))

# EXTRA CHALLENGE
import timeit
# Testing the speed of execution in a set
speed_test = '''
a = range(1000000) b = set(a)
i = 999999
for i in b:
print('')
'''
print(timeit.timeit(stmt=speed_test, number=3))