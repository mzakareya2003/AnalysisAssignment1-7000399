'''Mohamed Ihab Seifedlin Zakaria 7000399 T2 Analysis Assignment 2'''
def sequenceAlignment(x, y, delta):
    m = len(x)
    n = len(y)

    resultMatrix = [ [0 ] * (n+1) for i in range(m+1) ] # initialise the Result Matrix with zeros
    statusMatrix = [ [''] * (n+1) for i in range(m+1) ] # initialise the score Matrix with '' (aligned OR gapY OR gapX)

    # just to know what is connected to what
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 3 possibilities of alignment: x and y /// x and - /// - and y
            match = resultMatrix[i-1][j-1] + delta[x[i-1]][y[j-1]] # current x and current y
            gapY  = resultMatrix[i-1][ j ] + delta[x[i-1]]['-']    # current x and next y
            gapX  = resultMatrix[ i ][j-1] + delta[ '-'  ][y[j-1]] # next x and current y
            
            resultMatrix[i][j] = max(match, gapY, gapX) # max score of the 3 possibilities
            # check with the maximum wether it's aligned, gap y, gap x
            if resultMatrix[i][j] == match:   
                statusMatrix[i][j] = 'aligned' # x and y are aligned (x and y)
            elif resultMatrix[i][j] == gapY: 
                statusMatrix[i][j] = 'gapY'    # x is connected to gap in y (x and -)
            else: 
                statusMatrix[i][j] = 'gapX'    # y is connected to gap in x (- and y)
            

    # to get the aligned sequences(in reverse now)
    alignedX = ''
    alignedY = ''
    i = m
    j = n

    while i > 0 or j > 0:
        if statusMatrix[i][j] == 'aligned': # concatenate alignedX to x and alignedY to y
            alignedX = x[i-1] + alignedX
            alignedY = y[j-1] + alignedY
            i -= 1
            j -= 1
        elif statusMatrix[i][j] == 'gapY':  # concatenate alignedX to x and alignedY to - (y is gap)
            alignedX = x[i-1] + alignedX
            alignedY =  '-'   + alignedY
            i -= 1
        else:                               # concatenate alignedX to - and alignedY to y (x is gap)
            alignedX =  '-'   + alignedX
            alignedY = y[j-1] + alignedY
            j -= 1
            

    # now that we know the optimal sequences we calculate the alignment score according to the sequences
    alignmentScore = 0
    for z in range(len(alignedX)):
        alignmentScore += delta[alignedX[z]][alignedY[z]] 
        

    return alignedX, alignedY, alignmentScore



#seqA = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC" # ---TCCCAGTTATGTCAGGGGACACG-AG-CATG-CAGAGAC
#seqB = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC" # AATTGCC-G-C-CGTC-GTTTTCA-GCAGTTATGTCAGAT-C
seqA = "ATGCC"  # -ATGCC-
seqB = "TACGCA" # TACG-CA
delta = {
    'A': {'A': 1,    'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1,    'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1,    'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1,    '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1,   '-': 0}
        }
# calling the method
output = sequenceAlignment(seqA, seqB, delta)
print("")
print("Sequence X:", output[0])
print("Sequence Y:", output[1])
print("Alignment Score:", output[2])
print("")
