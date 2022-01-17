graph={}  
graph["start"]={}  
graph["start"]["a"]=6  
graph["start"]["b"]=2  
graph["a"]={}  
graph["a"]["fin"]=1  
graph["b"]={}  
graph["b"]["a"]=3  
graph["b"]["fin"]=5  
graph["fin"]={}
infinity=float("inf")  
costs={}  
costs["a"]=6  
costs["b"]=2  
costs["fin"]=infinity  
parents={}  
parents["a"]="start"  
parents["b"]="start"  
parents["fin"]=None  
procesed = []

def Dijstra_find(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in procesed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
        
def Dijstra(costs):
    node = Dijstra_find(costs)
    while node is not None:
        cost = costs[node]
        neighdors = graph[node]

        for n in neighdors.keys():
            new_cost = cost + neighdors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        procesed.append(node)
        node = Dijstra_find(costs)
    return costs["fin"],parents["fin"]
print(Dijstra(costs))
