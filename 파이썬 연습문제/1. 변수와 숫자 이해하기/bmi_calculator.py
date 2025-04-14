weight = float(input("체중(kg): "))
height = float(input("키(cm): ")) / 100  # cm를 m로 변환
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")