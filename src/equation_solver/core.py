from dataclasses import dataclass
from sympy import Eq, symbols, solve

@dataclass
class EquationDefinition:
    name: str
    equation: Eq
    variables: dict
    parameters: dict

def solve_symbolic(eq_def: EquationDefinition, target: str):
    sym_target = eq_def.variables[target]
    return solve(eq_def.equation, sym_target)