---
name: math
description: >
  Verify mathematical derivations step-by-step using SymPy.
  Use this when users ask to verify proofs, check calculations,
  or solve symbolic math problems.
---

When the user asks you to verify or solve mathematical problems:

1. Use the bundled `verify.py` script for symbolic computation
2. Show step-by-step derivation
3. Verify the final result

## Usage

Run the verification script:

    # Check two expressions are equal
    ~/.claude/skills/math/verify.py eq "EXPR1" "EXPR2"

    # Simplify/expand expression
    ~/.claude/skills/math/verify.py simp "EXPR"

Always explain your reasoning alongside the output.
