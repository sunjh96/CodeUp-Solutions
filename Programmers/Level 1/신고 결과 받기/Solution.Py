import sys
from collections import defaultdict
input = sys.stdin.readline


def solution(id_list, report, k):
    report = list(set(report))
    report_cnt = defaultdict(int)
    report_id = defaultdict(list)
    ans = [0 for _ in range(len(id_list))]
    suspend = []

    for x in report:
        do_report, get_reported = x.split()

        report_cnt[get_reported] += 1
        report_id[do_report].append(get_reported)

        if report_cnt[get_reported] == k:
            suspend.append(get_reported)

    for x in suspend:
        for i in range(len(id_list)):
            if x in report_id[id_list[i]]:
                ans[i] += 1
    return ans


if __name__ == '__main__':

    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo",
              "frodo neo", "muzi neo", "apeach muzi"]
    k = 2

    print(solution(id_list, report, k))
