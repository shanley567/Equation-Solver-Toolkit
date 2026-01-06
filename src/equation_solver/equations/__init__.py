import pkgutil, importlib, inspect
from ..core import EquationDefinition

def discover_equations():
    equations = {}
    pkg = __name__
    for _, mod_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"{pkg}.{mod_name}")
        for name, obj in inspect.getmembers(module, inspect.isfunction):
            if name.endswith("_equation"):
                eq = obj()
                equations[eq.name] = eq
    return equations