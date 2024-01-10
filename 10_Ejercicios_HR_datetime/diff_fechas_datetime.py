# datetime: this module helps us to find the difference betwen two or more dates, 

from datetime import datetime

fecha_str1 = "Fri 01 May 2015 13:54:36 -0000"
fecha_str2 = "Sat 02 May 2015 15:43:21 -0000"
# fecha_str2 = "Sat 02 May 2015 13:54:36 -0000"

format_str = "%a %d %b %Y %H:%M:%S %z" 
# %a: corresponds to the name of the day
# %d: corresponds to the number of the day
# %b: corresponds to the name of the month
# %Y: corresponds to the number of the year
# %H:%M:%S corresponds to the hour, minuts and seconds of the moment
# %z: correspons to the time zone

# convert the dates to the format of datetime (format_str)

fecha_1 = datetime.strptime(fecha_str1, format_str)
fecha_2 = datetime.strptime(fecha_str2, format_str)

difference = fecha_1 - fecha_2
diff_seconds = difference.total_seconds()

print(abs(diff_seconds))