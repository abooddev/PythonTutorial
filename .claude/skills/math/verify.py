#!/usr/bin/env python3
"""Symbolic math verification helper backed by SymPy.

Subcommands:
    eq   EXPR1 EXPR2   Check two expressions are mathematically equal.
    simp EXPR          Simplify the expression.
    expand EXPR        Expand the expression.
    solve EXPR VAR     Solve EXPR = 0 for VAR.
    diff  EXPR VAR     Differentiate EXPR with respect to VAR.
    integrate EXPR VAR Integrate EXPR with respect to VAR.
"""

from __future__ import annotations

import sys

from sympy import (
    diff,
    expand,
    integrate,
    simplify,
    solve,
    symbols,
    sympify,
)


def _parse(expr: str):
    return sympify(expr, convert_xor=True)


def _sym(name: str):
    return symbols(name)


def cmd_eq(a: str, b: str) -> int:
    lhs, rhs = _parse(a), _parse(b)
    diff_expr = simplify(lhs - rhs)
    equal = diff_expr == 0
    print(f"LHS         : {lhs}")
    print(f"RHS         : {rhs}")
    print(f"LHS - RHS   : {diff_expr}")
    print(f"Equal       : {equal}")
    return 0 if equal else 1


def cmd_simp(expr: str) -> int:
    e = _parse(expr)
    print(f"Input       : {e}")
    print(f"Simplified  : {simplify(e)}")
    return 0


def cmd_expand(expr: str) -> int:
    e = _parse(expr)
    print(f"Input       : {e}")
    print(f"Expanded    : {expand(e)}")
    return 0


def cmd_solve(expr: str, var: str) -> int:
    e = _parse(expr)
    v = _sym(var)
    sols = solve(e, v)
    print(f"Equation    : {e} = 0")
    print(f"Variable    : {v}")
    print(f"Solutions   : {sols}")
    return 0


def cmd_diff(expr: str, var: str) -> int:
    e = _parse(expr)
    v = _sym(var)
    print(f"Input       : {e}")
    print(f"d/d{v}      : {diff(e, v)}")
    return 0


def cmd_integrate(expr: str, var: str) -> int:
    e = _parse(expr)
    v = _sym(var)
    print(f"Input       : {e}")
    print(f"Integral    : {integrate(e, v)}")
    return 0


COMMANDS = {
    "eq": (cmd_eq, 2),
    "simp": (cmd_simp, 1),
    "expand": (cmd_expand, 1),
    "solve": (cmd_solve, 2),
    "diff": (cmd_diff, 2),
    "integrate": (cmd_integrate, 2),
}


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0

    name, *rest = argv[1:]
    if name not in COMMANDS:
        print(f"Unknown subcommand: {name}", file=sys.stderr)
        print(__doc__, file=sys.stderr)
        return 2

    func, arity = COMMANDS[name]
    if len(rest) != arity:
        print(
            f"`{name}` expects {arity} argument(s), got {len(rest)}",
            file=sys.stderr,
        )
        return 2

    return func(*rest)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
