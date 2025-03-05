class SparseVector:
    def __init__(self, nums: list):
        self.dense = {key:value for key,value in enumerate(nums) if value != 0}
        print(self.dense)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for key in self.dense.keys():
            if key in vec.dense.keys():
                result += self.dense[key] * vec.dense[key]
        return result

# Your SparseVector object will be instantiated and called as such:
v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
ans = v1.dotProduct(v2)
print(ans)