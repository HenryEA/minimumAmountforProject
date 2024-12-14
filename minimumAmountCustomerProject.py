def minAmt(numofProjects, projectId, bid) :
#1 match the projectID to the corresponding bid(s) and put it into a hashmao

#1a create a map and map every index to an empty array
    projects = {}

    for i in range(numofProjects):
        projects[i]= []

#1b populate the dictionary with bids for each project
    for i in range(len(projectId)):
        projects[projectId[i]].append(bid[i])

    totalCost = 0

#2a check in the projects map that was just created. If the projectId(key)
# does not have a corresponding value, then return -1
    for i in range(numofProjects):
        if not projects[i]:
            return -1
#2b get the minimum among the values of each projects[i]
        minbid = min(projects[i])
# add the minimum bid to total cost
        totalCost += minbid
#return total cost
    return totalCost

numofProjects = 5
projectId = [3, 2, 4, 2, 4, 1, 4, 1, 4, 4]
bid = [77, 82, 71, 44, 72, 25, 38, 88, 19, 43]
print(minAmt(numofProjects, projectId, bid))


numofProjects = 5
projectId = [0, 0, 4, 2, 3, 2, 0, 1, 2, 2]
bid = [77, 6, 63, 7, 10, 26, 90, 5, 53, 76]
print(minAmt(numofProjects, projectId, bid))
