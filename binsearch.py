'''binary search'''
''''take a ordered list and tell if a num is in that list or not'''

def bins(num, inl):
    l=len(inl)
    m=l/2
    if m==0 and num!=inl[m]: return False
    if num > inl[m]: 
        inl=inl[m:l]
        bins(num,inl)
    if num < inl[m]: 
        inl=inl[0:m]
        bins(num,inl)
    elif num==inl[m]: return True
    else: return False
    
def main():
    inl=[0,2,3,4,5,6]
    num=1
    if bins(num,inl): print "N is present"
    else: print "N is not present"

#if __name__==main: main()
    
main()
