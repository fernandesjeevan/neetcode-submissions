class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])* len(matrix)-1
        
        while(left<=right):
            mid = left + (right-left)//2
            tar_mat = mid//len(matrix[0])
            tar_pos = mid%len(matrix[0])
            print(left,mid,right,tar_mat,tar_pos)
            if matrix[tar_mat][tar_pos]==target:
                return True
            elif matrix[tar_mat][tar_pos]>target:
                right = mid-1
            else:
                left = mid+1
            
        return False
         

        
        