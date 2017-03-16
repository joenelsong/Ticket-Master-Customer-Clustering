val_ranges = [2,2,2,2]
stride = {0: 1, 1: 2, 2: 4, 3: 8}

scope = [0, 1, 2, 3]
vals= [1.89,0.135,4.41,0.315,5.742,13.398,0.198,0.462,3.15,0.225,7.35,0.525,4.698,10.962,0.162,0.378]
new_scope = [0, 1, 3]

#scope = [3,2]
#vals= [1.5, 2.5, 1.1, 0.9]
#new_scope = [3]


var = 2

new_vals = [0]* ( int(len(vals) / val_ranges[var])    ) # preparing for reduced size factor vals
old_indices = [ [0]*len(vals) for i in range( len(scope) ) ]


# Create old_indices
for i in range (len (scope)):
    stride_count = 0
    cur = 0
    for e in range( len(vals)):
        if (stride[ scope[i] ] == stride_count):
            cur = cur + 1 if (cur+1 < val_ranges[i]) else 0
            stride_count = 0
        old_indices[i][e] = cur
        stride_count = stride_count + 1
        
# Create new stride
curr_stride = 1
new_stride = {}
for v in new_scope:
    new_stride[v] = curr_stride
    curr_stride *= val_ranges[v]
    
# Create new_indices
new_indices = [ [0]*len(new_vals) for i in range( len(new_scope) ) ]

for i in range (len (new_scope)):
    stride_count = 0
    cur = 0
    for e in range( len(new_vals)):
        if (new_stride[ new_scope[i] ] == stride_count):
            cur = cur + 1 if (cur+1 < val_ranges[i]) else 0
            stride_count = 0
        new_indices[i][e] = cur
        stride_count = stride_count + 1
                




# populate new_vals by checking for indice matches
old_indices = np.delete(old_indices, scope.index(var), 0)
indices = np.array(indices)        
for i in range (len(vals) ):
    sum = 0
    if( old_indices[:,i].all() == new_indices[:,i].all() ):
        sum += vals[i]
        
        
