N = 20
total_g = 0
total_n = 0
grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
for _ in range(N):
    _obj, n, g = input().split()
    if g == "P":
        continue
    n = float(n)
    total_g += n * grade[g]
    total_n += n

print(round(total_g / total_n, 6))