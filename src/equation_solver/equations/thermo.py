from sympy import symbols, Eq
from ..core import EquationDefinition

def ideal_gas_equation():
    P, V, n, R, T = symbols("P V n R T")
    eq = Eq(P * V, n * R * T)
    variables = {"P": P, "V": V, "n": n, "R": R, "T": T}
    return EquationDefinition("ideal_gas", eq, variables, {})