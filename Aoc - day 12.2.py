def read_file(file):
    #read the file and put the information in a list
    with open(file, 'r') as input:
        input = list(input)
        raw_lines= []
        for line in input:
            line = line.rstrip()
            half_line= line.split('-')
            raw_lines.append(half_line)
        return raw_lines

def create_clusters(listed_data):
    # Take all values into a list
    all_item= []
    for dual in listed_data:
        for item in dual:
            all_item.append(item)
    # Only have the nodes name one time
    set_nodes= set(all_item)
    nodes= list(set_nodes)
    #Create a dictonary with the node as a key and the value as the conections
    conections= {}
    for node in nodes:
        nvalues= []
        for nlist in listed_data:
            if node in nlist:
                if nlist.index(node)==1:
                    nvalues.append(nlist[0])
                else:
                    nvalues.append(nlist[1])
        conections[node]= nvalues    
    return conections

#Having the conection from the nodes, now we are generating the path
def count_path(node_dic, path= ['start']):
    final = 0
    for nvalue in node_dic[path[-1]]:
        if nvalue.isupper() or (nvalue != 'start' and dup_check(nvalue, path) is True):
            final +=1 if nvalue== 'end' else count_path(node_dic, path + [nvalue])
    return final
                    
def dup_check(value, route):
    route = route + [value]
    route_count= []
    for n in set(route):
        if n.islower():
            route_count.append(route.count(n))
    if route_count.count(2) < 2 and max(route_count) <= 2:
        return True
    else:
        return False

#print(read_file('/Users/bzabert/Documents/Python/Adevent of code/Day 12/Aoc - day 12- input.txt'))
data= read_file('/Users/bzabert/Documents/Python/Adevent of code/Day 12/Aoc - day 12- input.txt')
conec_nodes= create_clusters(data)
print(count_path(conec_nodes))