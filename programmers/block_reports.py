def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report_count_dict = {id: 0 for id in id_list}
    report_dict = {id: set() for id in id_list}
    blocked = set()

    # 신고된 대상 카운트
    for row in report:
        reporter, reported = row.split()
        if reported not in report_dict[reporter]:
            report_count_dict[reported] += 1
            report_dict[reporter].add(reported)
    # 정지된 대상 정리
    for id, cnt in report_count_dict.items():
        if cnt >= k:
            blocked.add(id)
    # 처리 결과 메일 카운트
    for i in range(len(id_list)):
        mails = len(report_dict[id_list[i]].intersection(blocked))
        answer[i] += mails
    #print(answer)
    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)