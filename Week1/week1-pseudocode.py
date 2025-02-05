




# Area of Triangle
BEGIN
    h = input(height)
    b = input(base)
    area = 1/2 * b * h
    print(area)
END




# Seconds into hour and minute unit
BEGIN
    s = input(seconds)
    hr = s // 3600
    min = s // 60
    print(hr, min)
END











# Max, min, avg
BEGIN
    num1, num2, num3 = input(numbers)
    max = max(num1, num2, num3)
    min = min(num1, num2, num3)
    avg = (num1 + num2 + num3)/3
    print(max, min, avg)
END











# Circle Area
BEGIN
    r = input(radius)
    area = π * r * r
    print(area)
END




# Rectangle Circumference
BEGIN
    w = input(width)
    l = input(length)
    circumference = 2 * (w + l)
    print(circumference)
END



