def sort(s):
        print(s)
        content = sorted(s)
        content = ''.join(content)
        print(content)
        
def permutation(a,b):
    if(len(a) != len(b)):
            print('not permutation')
            return False
    print('permutation')
    return sort(a) == sort(b)


sort('cab')
permutation('hello','ohell')
