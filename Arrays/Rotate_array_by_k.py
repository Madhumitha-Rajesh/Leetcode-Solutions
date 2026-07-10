def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n=len(arr)
    k=k%n

    l,r=0,k-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

    l,r=k,n-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    
    l,r=0,n-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

    return arr

    pass
