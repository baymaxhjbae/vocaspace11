
def study_complex():
    # 숫자 랜덤 고르고 문제 만들 리스트 추출
    import random
    number = random.randint(0, len(word_list) - 1)
    gather = word_list[number]
    eng, korean, sentence, date = gather.split(maxsplit=2)

    # 문제 출력
    print(sentence)
    answer = input("영어: ")

    # 정답 여부 판별 (공백 제거 및 대소문자 무시)
    if answer.strip().lower() == eng.lower():
        print("정답입니다")
    else:
        print("정답이 아닙니다")
        print(eng)