def radix_sort_binary(matrix):
    ro = len(matrix[0])
    co = len(matrix)
    for i in range(0,ro):
        left = []
        right = []
        for j in range(0,co):
            if matrix[j][ro-i-1] == '1':
                left.append(matrix[j])
            else:
                right.append(matrix[j])
        matrix = left+right
    return matrix


data = []
for line in open('a1data2.txt'):
    data.append(line.split())
row = len(data)
col = len(data[0][0])
#print row,col
matix_sort = [[]]
k = 0
for i in range(0,col):
    for j in range(0,row):
        matix_sort[k].append(data[j][0][i])
    matix_sort.append([])
    k+=1
matix_sort.pop()
matrix_ = radix_sort_binary(matix_sort)

k_matrix = [[]]
k = 0
for i in range(0,len(matrix_[0])):
    for j in range(0,len(matrix_)):
        if matrix_[j][i] == '1':
            k_matrix[k].append(str(j))
    if len(k_matrix[k])< len(matrix_):
        k_matrix[k].append('%')
        zlist = ['0']*(len(matrix_) - len(k_matrix[k]))
        k_matrix[k] = k_matrix[k]+zlist
    k+=1
    k_matrix.append([])
k_matrix.pop()
for i in k_matrix:
    print i
d = {}
tag = 1
for i in range(0,len(k_matrix[0])):
    for j in range(0,len(k_matrix)):
        if k_matrix[j][i] != '0' and k_matrix[j][i]!= '%':
            if k_matrix[j][i] in d:
                if d[k_matrix[j][i]] != k_matrix[j][i] +'+'+  str(i):
                    tag = 0
            else:
                d[k_matrix[j][i]] = k_matrix[j][i] +'+'+ str(i)
print d
if tag == 0:
    print "not a perfect phylogeny"
else:
    print "yes!it's a perfect phylogeny"