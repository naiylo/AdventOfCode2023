# AdventOfCode 19.12.2023

with open(r"./AdventOfCode2023/December_19/day19_1.txt") as fin:
    example1 = fin.read().strip()
   
with open(r"./AdventOfCode2023/December_19/day19_2.txt") as fin:
    example2 = fin.read().strip()

# Task one:

import re

def createRules(rule):
    rules = []
    for i in rule:
        try:
            rule = [i[0],i[1],i[2:].split(":")[0],i.split(":")[1]]
        except: rule = [i]
        rules.append(rule)
    return rules

def applyRule(part, rule):
    x = part[0]
    m = part[1]
    a = part[2]
    s = part[3]
    for i in rule:
        if len(i) == 1:
            # print(i[0])
            return i[0]
        next = rule[-1]
        specificRule = i[0] + i[1] + i[2]
        if eval(specificRule):
            # print(i[-1])
            return i[-1]
        else: continue
        
def summary(string):
    A = []
    R = []
    workflows, parts = string.split("\n\n")
    workflow = workflows.split("\n")
    part = parts.split("\n")

    dict = {}
    for i in workflow:
        referenceChar, rest = i.split('{', 1)
        key = rest.rstrip('}')
        dict[referenceChar] = key
    
    for i in part:
        numbers = re.findall(r'\d+', i)
        aktPart = [int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])]
        rules = createRules(dict["in"].split(","))
        while True:
            nextRule = applyRule(aktPart,rules)
            if nextRule == "R":
                R.append(i)
                break
            if nextRule == "A":
                A.append(i)
                break
            rules = createRules(dict[nextRule].split(","))
    
    total = 0
    for i in A:
        numbers = re.findall(r'\d+', i)
        numbers = [int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])]
        toAdd = sum(numbers)
        total += toAdd

    return total
        
# Task two:

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def buildWorkflowDictionary(workflows):
        workflowsDict = {}
        for workflow in workflows:
            parts = workflow.split('{')
            workflowName = parts[0].strip()
            rules = parts[1].rstrip('}').split(',')
            workflowRules = []
            for rule in rules:
                try: 
                    condition, destination = rule.split(':')
                    condition = condition.strip()
                    workflowRules.append((condition.strip(), destination.strip()))
                except: 
                    condition = None
                    destination = rule
                    workflowRules.append((condition, destination))
            workflowsDict[workflowName] = workflowRules
        return workflowsDict

def dfs_paths_to_A(G, current_node, path, all_paths, workflows):
    if current_node == 'A':
        all_paths.append(path)
        return
    for successor in G.successors(current_node):
        rules = workflows[current_node]
        for rule, destination in rules:
            if destination == successor:
                dfs_paths_to_A(G, successor, path + [(current_node, rule)], all_paths, workflows)


def build_workflow_graph(workflows):
    G = nx.DiGraph()
    for workflow, rules in workflows.items():
        G.add_node(workflow)  # Add the workflow as a node
        for _, destination in rules:
            if destination is not None:
                G.add_edge(workflow, destination)
    return G

def calculateDistinctCombinations(string):
    workflows, _ = string.split("\n\n")
    workflows = workflows.split("\n")
    dict = buildWorkflowDictionary(workflows)
    # Build a graph representation of the workflows
    graph = build_workflow_graph(dict)

    all_paths_to_A = []

    # You need to change the input to the rules of "in" for example in my example 2 in{x>1863:xq,gx} 
    # so it would be "dfs_paths_to_A(graph, successor, [('in', 'x>1863')], all_paths_to_A, dict)"

    for successor in graph.successors('in'):
        dfs_paths_to_A(graph, successor, [('in', 's<1351')], all_paths_to_A, dict)
    
    for path in all_paths_to_A:
        print("Path:", path)
        print()

    
if __name__ == "__main__":
    #print("Result with function summary:")
    #print("Example 1:")
    #print(summary(example1))
    #print("Example 2:")
    #print(summary(example2))
    #print("Result with function calculateDistinctCombinations:")
    #print("Example 1:")
    print(calculateDistinctCombinations(example1))
    #print("Example 2:")
    #print(calculateDistinctCombinations(example2))
    