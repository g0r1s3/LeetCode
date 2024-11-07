from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return date_obj.timetuple().tm_yday
