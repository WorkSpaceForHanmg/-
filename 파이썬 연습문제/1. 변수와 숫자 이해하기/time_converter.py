total_seconds = 12345
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{total_seconds}초는 {hours}시간 {minutes}분 {seconds}초입니다.")