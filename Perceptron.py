def MatrixMult(A, B):
    S = []
    for i in range(len(A)):
        Si = []
        for j in range(len(B[0])):
            Xij=0
            for k in range(len(B)):
                Xij = Xij + A[i][k]*B[k][j]
            Si.append(Xij)
        S.append(Si)
    return S

def MatrixMinus(A, B):
    S = []
    for i in range(len(A)):
        if(type(A[i]) != list):
            S.append(A[i]-B[i])
        else:
            Si = []
            for j in range(len(A[i])):
                Si.append(A[i][j] - B[i][j])
            S.append(Si)

    return S
    
def MatrixPlus(A,B):
    i = 0
    S = []
    if (type(A[0]) == int) & (type(B[0]) == int):
        while i<len(A):
            S.append(A[i]+B[i])
            i = i+1
        return S  
    elif type(A[0]) == list:
        while i<len(A):
            j = 0
            Si = []
            while j<len(A[0]):
                Si.append(A[i][j]+B[i][j])
                j=j+1
            S.append(Si)
            i = i+1
        return S
        
def MatrixMultNumber(a,A):
    S = []
    for i in range(len(A)):
        if(type(A[i]) == list):
            Si = []
            for j in range(len(A[i])):
                Si.append(A[i][j]*a)
            S.append(Si)
        else:
            S.append(A[i]*a)
    return S
       
def SignumIt(A):
    for i in range(len(A)):
        if type(A[i]) == int:
            if(A[i]>0):
                A[i] = 1
            else:
                A[i] = 0
        else:
            for j in range(len(A[i])):
                if(A[i][j]>0):
                    A[i][j] = 1
                else:
                    A[i][j] = 0    


XX = [
[[
1,1,1,1,
1,0,0,1,
1,0,0,1,
1,0,0,1
]],[[
1,1,1,0,
1,0,1,0,
1,1,1,0,
1,0,0,0
]],[[
1,0,0,1,
1,0,1,1,
1,1,0,1,
1,0,0,1
]],[[
1,1,1,0,
1,1,1,0,
1,0,1,0,
1,1,1,0
]]
]


FromFile = True
import pickle

if(not FromFile):

    W1 = [
    [0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0],
    [1,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1],
    [1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1],
    [1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1],
    [1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1],
    [1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0],
    [1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1]
    ]


    W2= [
    [0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0],
    [1,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1],
    [1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1],
    [1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1],
    [1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1],
    [1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0],
    [1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1]
    ]

    step = 0.01
    for i in range(5000):
        for X in XX:
            NumberOfInputs = len(X[0])
            Grad1 = []
            for i in range(NumberOfInputs):
                Grad1i = []
                for j in range(NumberOfInputs):
                    Grad1i.append(X[0][i])
                Grad1.append(Grad1i)
            S = MatrixMult(X,W1)
            SignumIt(S)
            Grad2 = []
            for i in range(NumberOfInputs):
                Grad2i = []
                for j in range(NumberOfInputs):
                    Grad2i.append(S[0][i])
                Grad2.append(Grad2i)
            M = MatrixMult(S,W2)       
            SignumIt(M)
            E = MatrixMinus(X,M)
            
            D2 = []
            for i in range(NumberOfInputs):
                Di = []
                for j in range(NumberOfInputs):
                    if i==j:
                        Di.append(E[0][i])
                    else:
                        Di.append(0)
                D2.append(Di)
            Grad = MatrixMult(Grad2,Grad1)
            CorrectionsMultipliers = MatrixMult(Grad2,D2)
            Corrections = MatrixMultNumber(step, CorrectionsMultipliers)
            W2 = MatrixPlus(W2, Corrections)
            CorrectionsMultipliers = MatrixMult(Grad,D2)
            Corrections = MatrixMultNumber(step, CorrectionsMultipliers)
            W1 = MatrixPlus(W1, Corrections)

    f = open('weights.txt', 'wb')
    Data = {
        'W1': W1,
        'W2': W2
        }
    pickle.dump(Data,f)
    f.close()
else:

    f = open('weights.txt', 'rb')
    Data = pickle.load(f)
    f.close()
    W1=Data['W1']
    W2=Data['W2']



Original = [[
1,1,1,1,
1,0,0,1,
1,0,0,1,
1,0,0,1
]]

Picture = [[
1,0,0,1,
1,0,1,0,
0,1,1,1,
1,0,1,0
]]

S = MatrixMult(Picture,W1)
SignumIt(S)
M = MatrixMult(S,W2)       
SignumIt(M)

S = MatrixMult(M,W1)
SignumIt(S)
M = MatrixMult(S,W2)       
SignumIt(M)


print(M)
print(Original)