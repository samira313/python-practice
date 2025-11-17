actual = list(map(int, input().split()))
expected = list(map(int, input().split()))

if actual[2] > expected[2]:
    print(50000)
elif actual[1] > expected[1]:
    print((actual[1] - expected[1]) * 4000)
elif actual[0] > expected[0]:
    print((actual[0] - expected[0]) * 200)
else:
    print(0)
