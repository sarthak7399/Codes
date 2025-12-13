# https://leetcode.com/problems/coupon-code-validator/

# Example 1:
# Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]
# Output: ["PHARMA5","SAVE20"]
# Explanation:
# First coupon is valid.
# Second coupon has empty code (invalid).
# Third coupon is valid.
# Fourth coupon has special character @ (invalid).

class Solution:
    def validateCoupons(self, code: List[str],
                        businessLine: List[str],
                        isActive: List[bool]) -> List[str]:
        # Lists for each valid business line
        e, g, p, r = [], [], [], []

        for i, active in enumerate(isActive):
            # Skip inactive coupons
            if not active:
                continue

            bl = businessLine[i]

            # Allow only supported business lines
            if bl not in {"electronics", "grocery", "pharmacy", "restaurant"}:
                continue

            # Code must be non-empty and contain only alphanumeric or '_'
            if not code[i] or not all(c.isalnum() or c == '_' for c in code[i]):
                continue

            # Group codes by business line initial
            if bl[0] == 'e':
                e.append(code[i])
            if bl[0] == 'g':
                g.append(code[i])
            if bl[0] == 'p':
                p.append(code[i])
            if bl[0] == 'r':
                r.append(code[i])

        # Return sorted codes in required order
        return sorted(e) + sorted(g) + sorted(p) + sorted(r)
