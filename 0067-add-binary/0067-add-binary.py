class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Relocate longer binary to a
        if len(a) < len(b): a, b = b, a

        carry = 0; ans = ""
        a_idx, b_idx = len(a) - 1, len(b) - 1
        while a_idx >= 0:
            if b_idx >= 0:
                num = int(a[a_idx]) + int(b[b_idx]) + carry 
                carry = num // 2; ans = str(num % 2) + ans
                b_idx -= 1
            else:
                if carry != 0:
                    num = int(a[a_idx]) + carry
                    carry = num // 2; ans = str(num % 2) + ans
                else:
                    ans = a[:a_idx + 1] + ans
                    return ans 
            a_idx -= 1
        
        if carry != 0: 
            ans = str(carry) + ans
        return ans