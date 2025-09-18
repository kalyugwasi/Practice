class Daa:
    def binaryS(self,nums:list,tar:int):
        print("Initial array = ",nums)
        print("Target : ",tar)
        
        for i in range(len(nums)-1):
            minVal = min(nums[i:])
            idx = nums.index(minVal)
            nums[i],nums[idx] = nums[idx],nums[i]


        print("Sorted array = ",nums)
        
        l,r = 0, len(nums) -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>tar:
                r = mid -1 
            elif nums[mid]<tar:
                l = mid +1
            if nums[mid] == tar:
                print("Found at index : ",end="")
                return mid
s = Daa()
print(s.binaryS([2,4,6,1,7,0,4,5,3,9,8],3))