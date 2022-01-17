def chanage_tickets(tickets):
    ticket_dic = {}
    for [key,item] in tickets:
        if key not in ticket_dic.keys():
            ticket_dic[key] = []
        ticket_dic[key].append(item)
    for array_d in ticket_dic.values() :
        array_d.sort()
    return ticket_dic
def dfs(start,ticket_dic,visited =[]):
    while start in ticket_dic.keys() and ticket_dic[start] != []:
        path = ticket_dic[start].pop(0)
        dfs(path,ticket_dic,visited)
    visited.insert(0,start)
def solution(tickets):
    visited = []
    tickets_dic = chanage_tickets(tickets)
    dfs("ICN",tickets_dic,visited)
    return visited

tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
print(chanage_tickets(tickets))
print(solution(tickets))