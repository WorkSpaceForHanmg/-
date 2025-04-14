def count_words(sentence):
    return len(sentence.split())

# 테스트
print(f"단어 수: {count_words('Python is fun and powerful')}")  # 5