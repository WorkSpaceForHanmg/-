id_number = "901212-1234567"
year = "19" + id_number[:2]
month = id_number[2:4]
day = id_number[4:6]
print(f"{year}년 {month}월 {day}일")