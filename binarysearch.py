#BINARY SEARCH

def binary(list,element,beg,end):
    '''Objective : search an object using binary search
       Input: list- list in which you have to search
               beg: starting index of the list
               end: ending position of the list
       Return value: Return the position of the founded element
    '''

    #Approach: divide the list into two parts using a variable mid
    #mid is the middle element, if middle element of list < element
    #we have to search the element in the next part else in the first
    #part. Repeat the steps unless middle element== element else
    #return -1
    mid=(beg+end)//2
    if beg<end:
        if list[mid]==element:
            return print("Element foound at position",mid)
        
        if list[mid]>element:
            binary(list,element,beg,mid)
        else:
            binary(list,element,mid+1,end)
    else:
        print("OOPS... ELEMENT NOT FOUND")

def main():
    list=[5,10,15,20,70,80,90]
    print(list)
    element=int(input("Enter element you want to search"))
    binary(list,element,0,len(list))
        

if __name__=='__main__':
    main()
        
    
