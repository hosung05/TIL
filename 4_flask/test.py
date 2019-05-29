real_numbers = set([1, 2, 3, 4, 5, 6])
bonus_number = 8

lucky_numbers = set([1, 2, 3, 4, 5, 6])

match_count = len(real_numbers.intersection(lucky_numbers))

if match_count == 6:
    print(1)
elif match_count == 5 and bonus_number in lucky_numbers:
    print(2)
elif match_count == 5:
    print(3)
elif match_count == 4:
    print(4)
elif match_count == 3:
    print(5)
else:
    print('꽝')


# real 과 lucky 가
# 1등: 6개가 같다.
# 2등: 5개가 같고, 나머지 하나가 bonus 다.
# 3등: 5개가 같다.
# 4등: 4개가 같다.
# 5등: 3개가 같다.
