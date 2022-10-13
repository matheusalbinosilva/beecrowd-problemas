N = int(input())
r = 0

if N >= 3600:
    h = N / 3600
    r = (h*3600) - 3600
if r >= 60:
    m = 