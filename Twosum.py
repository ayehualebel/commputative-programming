class Solution(object):
    def findOriginalArray(self, changed):
        self.changed=changed
        if len(changed) % 2 != 0:
            return []
    
        original = []
        count = Counter(changed)
    
        for num in sorted(changed):
            if count[num] == 0:  # If this num has already been used
                continue
        
            if count[num * 2] == 0:  # If the doubled value doesn't exist
                return []
        
            original.append(num)
            count[num] -= 1
            count[num * 2] -= 1
    
        return original
