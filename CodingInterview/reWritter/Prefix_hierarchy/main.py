# Prefix matching 
# output int list 

# ['Martin', 'Pedro', 'Maria', 'Martina', 'Marina', 'Mongo']
# Prefix ['Mart', 'Mar', 'Mong']
# Output: [2, 4, 1]


def prefix_hierarchy(input_list, query):
    """
    input_list: list of strings
    query: list of strings
    output: list of int
    """
    output = []
    counter = 0

    for j in range(len(query)):
        for i in range(len(input_list)):
            if (input_list[i].startswith(query[j]) and  (len(input_list[i]) != len(query[j]))):
                counter += 1
        output.append(counter)
        counter = 0
        
    return output

print(prefix_hierarchy(['Martin', 'Pedro', 'Maria', 'Martina', 'Marina', 'Mongo'], ['Mart', 'Mar', 'Mong']))