"""
The main search program
"""
class DFSPruning():
    def __init__(self):
        self.solutions = []
        self.num_branches_pruned = 0

    def dfs_with_prune(self, state, domain, var_i):
        # Check if any constraint is violated
        if self.has_violated_constraint(state):
            self.num_branches_pruned += 1
            return   # Prune this branch by returning prematurely
        
        # Check if all variables have been assigned a value
        if var_i == len(state):
            self.solutions.append(state) # A solution is found.
            return

        # Not all variables have values yet. Continue assigning
        for value in domain:
            new_state = dict.copy(state)
            letter = chr(var_i + 65) # Magic number for ASCII conversion
            new_state[letter] = value
            self.dfs_with_prune(new_state, domain, var_i + 1) # Recursive call

        # Solutions are stored solutions in class variable
        return None
    
    # Checks if any constraints have been violated.
    def has_violated_constraint(self, state):
        return (( # All constraints in their negative form
            self.is_defined(state, ["A","G"]) and state["A"] <= state["G"]) or (
            self.is_defined(state, ["A","H"]) and state["A"] > state["H"]) or (
            self.is_defined(state, ["F","B"]) and abs(state["F"] - state["B"]) != 1) or (
            self.is_defined(state, ["G","H"]) and state["G"] >= state["H"]) or (
            self.is_defined(state, ["G","C"]) and abs(state["G"] - state["C"]) != 1) or (
            self.is_defined(state, ["H","C"]) and abs(state["H"] - state["C"]) % 2 != 0) or (
            self.is_defined(state, ["H","D"]) and state["H"] == state["D"]) or (
            self.is_defined(state, ["D","G"]) and state["D"] < state["G"]) or (
            self.is_defined(state, ["D","C"]) and state["D"] == state["C"]) or (
            self.is_defined(state, ["E","C"]) and state["E"] == state["C"]) or (
            self.is_defined(state, ["E","D"]) and state["E"] >=state["D"] - 1) or (
            self.is_defined(state, ["E","H"]) and state["E"] == state["H"] - 2) or (
            self.is_defined(state, ["G","F"]) and state["G"] == state["F"]) or (
            self.is_defined(state, ["H","F"]) and state["H"] == state["F"]) or (
            self.is_defined(state, ["C","F"]) and state["C"] == state["F"]) or (
            self.is_defined(state, ["D","F"]) and state["D"] == state["F"] - 1) or (
            self.is_defined(state, ["E","F"]) and abs(state["E"] - state["F"]) % 2 != 1))
    
    # Returns true if all vars in state have an assigned value 
    def is_defined(self, state, vars):
        for v in vars:
            if state[v] == - 1:
                return False
        return True

"""
Setup
"""
search = DFSPruning()
initial_state = {"A":-1,"B":-1,"C":-1,"D":-1,"E":-1,"F":-1,"G":-1,"H":-1}
domain = [1,2,3,4]

"""
Call
"""
search.dfs_with_prune(initial_state, domain, 0)

for s in search.solutions:
    print(s)
print(search.num_branches_pruned)
