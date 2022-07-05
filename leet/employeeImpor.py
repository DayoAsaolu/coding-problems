class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

    def __str__(self):
        str = f"[id:{self.id}, imp:{self.importance}] --> sub:{self.subordinates}"
        # for i in self.subordinates:
        #     str += f" [id:{i.id}, imp:{i.importance}]"
        
        return str
        # return f"id: {self.id}, imp: {self.importance} --> [ sub: {self.subordinates} ]"

def getImportance(employees, id):
    # find the employee in the tree and return
    # using dfs or bfs to navigate all the child nodes from the employee
    # keep add the importance of each subordiantes plus the employee importance to a global varibale
    # return the global varibale
    
    def contrustEmployeMap(employees):
        hashMap = {}

        for employee in employees:
            hashMap[employee.id] = ( employee.importance, employee.subordinates )
            
        return hashMap

    for i in contrustEmployeMap(employees):
        print("no--> ", contrustEmployeMap(employees)[i], "\n")


    def findEmployee(employees, id):
        treeStack = [ employees ]
        while len(treeStack) != 0:
            curr = treeStack.pop()
            if curr.id == id:
                return curr
            else:
                for i in curr.subordinates:
                    treeStack.append(i)
            
        return []
    
    # found = findEmployee(employees, 1)
    # print("found employee : ", found)

    def addImportance(id):
        graph = contrustEmployeMap(employees)
        if id not in graph: return "id not in graph"

        total = 0
        treeStack = [ graph[id] ]
        while len(treeStack) != 0:
            curr = treeStack.pop()
            print("curr-- ", curr)
            total += curr[0]
            for i in curr[1]:
                treeStack.append(graph[i])

        return total

    print("total importance-- ", addImportance(id))


def main():
    E1 = Employee(3,3,[])
    E2 = Employee(2,3,[])
    E3 = Employee(1,5,[2,3])
    l = [E3, E2, E1]

    print("E1: ", l)

    print("get employee ",getImportance(l, 4))

    return 0 

main()