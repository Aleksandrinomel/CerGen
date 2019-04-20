import random

start = 4
end = 7
mdop = True
mdo = 0.2
npoints = 1
rnd = 3


def points(start, end, mdop, mdo, npoints, rnd):
    mdo_rnd = round(mdo, rnd)
    list_of_points_ref = [start, end]
    s_n = start - end
    list_of_points_dev = []
    list_of_points_delta = []
    point = start
    all_points = {}

    for i in range(npoints - 2):
        point += ((end - start) / (npoints - 1))
        list_of_points_ref.append(round(point, rnd))
        list_of_points_ref.sort()

    if mdop:
        mdo /= 100
        for j in list_of_points_ref:
            rand = random.uniform(-s_n * mdo, s_n * mdo)
            list_of_points_dev.append(round(j + rand, rnd))
        for i in range(len(list_of_points_ref)):
            list_of_points_delta.append(
                round(abs(abs(list_of_points_ref[i]) - abs(list_of_points_dev[i])) * 100 / s_n, rnd))
    else:
        for j in list_of_points_ref:
            rand = random.uniform(-mdo, mdo)
            list_of_points_dev.append(round(j + rand, rnd))
        for i in range(len(list_of_points_ref)):
            list_of_points_delta.append(round(abs(abs(list_of_points_ref[i]) - abs(list_of_points_dev[i])), rnd))

    for n in range(npoints):
        all_points[n + 1] = [list_of_points_ref[n], list_of_points_dev[n], list_of_points_delta[n], mdo_rnd]

    return all_points


d = points(start,end,mdop,mdo,npoints,rnd)
print(d)