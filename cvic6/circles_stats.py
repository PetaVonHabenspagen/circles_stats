def radius_sum(r1, r2):
    radius = r1 + r2
    return radius

def euclid_distance(x1, y1, x2, y2):
    import math
    distance = []
    distance.append(abs(x1 - x2))
    distance.append(abs(y1 - y2))
    sqroot = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    return round(sqroot, 2)

def has_intersection(circle1, circle2):
    pruniky = {

    }
    if euclid_distance > radius_sum:
        pruniky[circle1] = 0
        pruniky[circle2] = 0
    elif euclid_distance == radius_sum:
        print(":)")

print(euclid_distance(1, 3, 7, 9))
