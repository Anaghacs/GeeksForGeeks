#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

solution = Solution

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends