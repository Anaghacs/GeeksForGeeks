#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
		first = second = -1
        
        for i in range(n):
            if arr[i] > first:
                second = first
                first = arr[i]
            elif arr[i] > second and arr[i] != first:
                second = arr[i]
        
        return second

sol = Solution()


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends