def kadane(array):
    msf = 0
    meh = 0
    for i in array:
        meh = max(meh+i,i)
        msf = max(msf,meh)
    return msf
