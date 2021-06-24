class Job:
    def __init__(self, start, finish, profit):
        self.start  = start
        self.finish = finish
        self.profit  = profit
def binary_search(job, start_index):
    lo = 0
    hi = start_index - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1
def schedule(job):
    job = sorted(job, key = lambda j: j.finish)
    n = len(job) 
    table = [0 for _ in range(n)]
    table[0] = job[0].profit
    for i in range(1, n):
        incl_prof = job[i].profit
        l = binary_search(job, i)
        if (l != -1):
            incl_prof += table[l]
        table[i] = max(incl_prof, table[i - 1])
    return table[n-1]