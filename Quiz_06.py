def 주민번호_검증(resident_number):
    if len(resident_number) != 13:
        return False

    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    try:
        numbers = list(map(int, list(resident_number)))
    except ValueError:
        return False

    # 마지막 자리의 수를 제외한 숫자들에 가중치를 적용하고 합산
    weighted_sum = sum(a * b for a, b in zip(numbers[:-1], weights))

    # 11로 나눈 나머지를 구하고 11에서 나머지를 빼줍니다.
    remainder = (11 - (weighted_sum % 11)) % 10

    # 계산된 결과와 주민등록번호의 마지막 자리를 비교
    return remainder == numbers[-1]

# 주민등록번호를 입력받아 유효성을 검사
resident_number = input("주민등록번호를 입력하세요: ")
if 주민번호_검증(resident_number):
    print("주민등록번호가 유효합니다.")
else:
    print("주민등록번호가 유효하지 않습니다.")
