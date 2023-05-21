def merge(intervals):
    intervals = sorted(intervals)
    out = [intervals[0]]
    for li in intervals[1:]:
        if out[-1][1] >= li[0]:
            buildli =[]
            if  out[-1][1] <= li[1]:
                buildli.append(out[-1][0])
                buildli.append(li[1]) 
                out[-1] = buildli
        else:
            out.append(li)
    return out

# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[2,3]]

print(merge(intervals))