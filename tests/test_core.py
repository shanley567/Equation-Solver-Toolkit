from equation_solver.equations import discover_equations

def test_discover_equations_finds_ideal_gas():
    equations = discover_equations()
    assert "ideal_gas" in equations