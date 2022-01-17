def dfs(now, graph, save_path) :
    while now in graph.keys() and graph[now] != [] :
        path = graph[now][0]
        graph[now] = graph[now][1:]
        dfs(path, graph, save_path)
    save_path.insert(0, now)

def solution(tickets):
    graph = {}
    for [src, dst] in tickets :
        if not src in graph.keys() :
            graph[src] = []
        graph[src].append(dst)

    for array_destn in graph.values() :
        array_destn.sort()

    # graph_keys = sorted(graph.keys())

    # new_graph = {}
    # for key in graph_keys :
    #     new_graph[key] = graph[key]

    retrn = []
    dfs("ICN", graph, retrn)

    answer = retrn
    return answer

t =[['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]
print(solution(t))