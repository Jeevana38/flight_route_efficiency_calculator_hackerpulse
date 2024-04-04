def dijkstra(source_index,dest_index,locations):
    global adj,fuel
    visited=[]
    path=[]
    prev=[]
    for i in range(len(locations)):
        visited.append(False)
        path.append(99999999)
        prev.append(source_index)
    path[source_index]=0
    for i in range(len(locations)):
        visited[i]=True
        for j in range(len(locations)):
            if adj[i][j] < 99999999 and (visited[j]==False) and path[j]>path[i]+ adj[i][j]:
                prev[j]=i
                path[j]=path[i] +adj[i][j]

    route=[dest_index]
    j=dest_index
    while j != source_index:
        j = prev[j]
        route.append(j)
    route=route[::-1]
    fuel = path[dest_index]
    if fuel >= 99999999:
        fuel = 0
        return "NO POSSIBLE ROUTE"
    final_route = []

    for index in route[:-1]:
        final_route.append(locations[index].title())
    final_route.append(locations[index+1].title())
    return final_route


#routes=[("New York", "London", 500), ("London", "Paris", 100), ("Paris", "Berlin", 50), ("New York", "Paris", 600), ("Berlin", "Tokyo", 250)]

routes = []
total_routes = int(input("Enter number of routes: "))

while total_routes > 0:
    route_source = input("Enter route source: ").lower()
    route_destination = input("Enter route destination: ").lower()
    route_fuel = int(input("Enter fuel: "))
    print("\n")
    routes.append((route_source,route_destination,route_fuel))
    total_routes -= 1
source = input("Enter source: ").lower()
destination = input("Enter destination: ").lower()
print("\n")
locations = []
for route in routes:
    if route[0] not in locations:
        locations.append(route[0])
    if route[1] not in locations:
        locations.append(route[1])
adj=[]
for i in range(len(locations)):
    l=[99999999 for i in range(len(locations)) ]
    adj.append(l)

for route in routes:
    source_index = locations.index(route[0])
    dest_index = locations.index(route[1])
    adj[source_index][dest_index] = route[2]
source_index = locations.index(source)
dest_index = locations.index(destination)
fuel = 0
route = dijkstra(source_index,dest_index,locations)
print("Route: ",route)
print("Total Fuel Consumption: ",fuel)



