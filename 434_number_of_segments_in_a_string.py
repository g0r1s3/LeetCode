class Solution:
    def countSegments(self, s: str) -> int:
        list_of_segments = s.split()
        return len(list_of_segments)
