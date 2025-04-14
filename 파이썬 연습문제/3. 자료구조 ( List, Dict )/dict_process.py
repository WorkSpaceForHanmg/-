# 딕셔너리 값 출력
person = {"name": "John", "age": 30}
print(f"나이: {person['age']}")

# 딕셔너리 키 출력
scores = {"math": 90, "science": 85, "history": 78}
print(f"과목들: {list(scores.keys())}")

# 딕셔너리 값 변경
fruits = {'apple': 3, 'banana': 5}
fruits['apple'] += 2
print(fruits)