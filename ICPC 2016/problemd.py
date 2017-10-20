def returnFolds(A):
    folds = 0
    for i,v in enumerate(A):
        if i == 0:
            prev = None
        else:
            prev = A[i-1]
        if v != prev:
            folds += 1
    return folds

if __name__ == "__main__":
    A = [1,0,0,1]
    print(returnFolds(A))