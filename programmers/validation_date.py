def due_date(date, term, terms_dict):
    year, month, day = map(int, date.split('.'))
    days = day + (month-1)*28 + (year-1)*(28*12) + terms_dict[term]*28
    n_year = str(days // (28*12) + 1)
    n_month = str((days % (28*12)) // 28 + 1)
    n_day = str((days % (28*12)) % 28)
    if len(n_month) == 1:
        n_month = '0' + n_month
    if len(n_day) == 1:
        n_day = '0' + n_day
    return n_year + '.' + n_month + '.' + n_day

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for term in terms:
        id, month = term.split()
        terms_dict[id] = int(month)
    for i in range(len(privacies)):
        date, id = privacies[i].split()
        #print(today, due_date(date, id, terms_dict))
        if today >= due_date(date, id, terms_dict):
            answer.append(i+1)
    #print(answer)
    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])