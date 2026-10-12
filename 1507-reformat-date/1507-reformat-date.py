class Solution:
    def reformatDate(self, date: str) -> str:
        parts=date.split()
        day=""
        for char in parts[0]:
            if char.isdigit():
                day+=char
        if len(day) == 1:
            day = "0" + day
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03",
            "Apr": "04", "May": "05", "Jun": "06",
            "Jul": "07", "Aug": "08", "Sep": "09",
            "Oct": "10", "Nov": "11", "Dec": "12"
        }
        month=months[parts[1]]
        year=parts[2]
        ans = year + "-" + month + "-" + day
        return ans 


        