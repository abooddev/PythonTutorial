# 7th Grade Mathematics Exam — Detailed Solutions

> Every numerical step in this document was verified symbolically with SymPy
> (`.claude/skills/math/verify.py`).

---

## Part A — Proportionality & Proportion Coefficient

### Question 1 (4 pts)

| Time `t` (h) | 2 | 3 | 5 | 7 |
|---|---|---|---|---|
| Distance `d` (km) | 70 | 105 | 175 | 245 |

**a) Is the relationship proportional?**
Compute the ratio `d / t` for every column:

$$\frac{70}{2} = 35 \quad ; \quad \frac{105}{3} = 35 \quad ; \quad \frac{175}{5} = 35 \quad ; \quad \frac{245}{7} = 35$$

All four ratios are equal, so **yes, the relationship is proportional**.

**b) Proportion coefficient.**
The constant ratio is the coefficient: **`k = 35`** (kilometers per hour).

**c) Formula.**

$$\boxed{\, d = 35 \cdot t \,}$$

---

### Question 2 (4 pts)

The table is proportional with `k = 3`, so `y = 3 · x`.

| x | 2 | **4** | **7** | 10 |
|---|---|-----|-----|----|
| y | 6 | **12** | 21 | **30** |

Steps:
- `x = 4 → y = 3 · 4 = 12`
- `y = 21 → x = 21 / 3 = 7`
- `x = 10 → y = 3 · 10 = 30`

---

### Question 3 (4 pts)

$$\frac{4}{10} = \frac{x}{25}$$

Cross-multiply:

$$10 \cdot x = 4 \cdot 25 \quad \Longrightarrow \quad 10x = 100 \quad \Longrightarrow \quad x = \frac{100}{10} = \boxed{10}$$

---

### Question 4 (4 pts)

**Coefficient (flour per cookie):**

$$k = \frac{150 \text{ g}}{4 \text{ cookies}} = 37.5 \text{ g/cookie}$$

**For 18 cookies:**

$$\text{flour} = 18 \cdot 37.5 = \boxed{675 \text{ g}}$$

Verification by cross-multiplication: `(18 · 150) / 4 = 2700 / 4 = 675`. ✓

---

### Question 5 (4 pts)

**Table a)** `y/x = 3/1 = 6/2 = 9/3 = 12/4 = 3`. Constant → **proportional**, `k = 3`.

**Table b)** Ratios `y/x`:

$$\frac{3}{1}=3,\quad \frac{4}{2}=2,\quad \frac{5}{3}\approx 1.67,\quad \frac{6}{4}=1.5$$

Ratios are **not constant** → **not proportional**.
(The pattern here is `y = x + 2`, an additive relation, not multiplicative.)

---

## Part B — Percentages

### Question 6 (3 pts)

$$25\% \text{ of } 80 \;=\; \frac{25}{100} \cdot 80 \;=\; \frac{1}{4} \cdot 80 \;=\; \boxed{20}$$

---

### Question 7 (4 pts)

Fraction wearing glasses:

$$\frac{15}{60} = \frac{1}{4}$$

Convert to a percentage:

$$\frac{1}{4} = \frac{25}{100} = \boxed{25\%}$$

---

### Question 8 (5 pts)

A 12 % increase multiplies the price by `1 + 12/100 = 1.12`.

$$\text{new price} = 200 \cdot 1.12 = \boxed{224 \text{ €}}$$

Alternative (two-step):
- Increase amount: `12/100 · 200 = 24 €`
- New price: `200 + 24 = 224 €` ✓

---

### Question 9 (4 pts)

A 20 % discount multiplies the price by `1 − 20/100 = 0.80`.

$$\text{final price} = 50 \cdot 0.80 = \boxed{40 \text{ €}}$$

Alternative: discount `= 20/100 · 50 = 10 €`, so `50 − 10 = 40 €`. ✓

---

### Question 10 (4 pts)

$$30\% \text{ of } 250 \;=\; \frac{30}{100} \cdot 250 \;=\; \frac{3}{10} \cdot 250 \;=\; \boxed{75 \text{ students}}$$

---

## Part C — Polynomials Basics

Given `P(x) = 3x² + 2x − 1` and `Q(x) = x² − 5x + 4`.

### Question 11 (3 pts)

`P(x) = 3x² + 2x − 1`.
- **Degree** = highest power of `x` = **2**.
- **Leading coefficient** = coefficient of `x²` = **3**.

---

### Question 12 (4 pts) — `P(x) + Q(x)`

Group like terms:

$$P + Q = (3x^2 + x^2) + (2x + (-5x)) + (-1 + 4)$$

$$= 4x^2 + (-3x) + 3$$

$$\boxed{P(x) + Q(x) = 4x^2 - 3x + 3}$$

---

### Question 13 (4 pts) — `P(x) − Q(x)`

Distribute the minus sign first:

$$P - Q = 3x^2 + 2x - 1 \;-\; x^2 + 5x - 4$$

Group like terms:

$$= (3x^2 - x^2) + (2x + 5x) + (-1 - 4)$$

$$= 2x^2 + 7x - 5$$

$$\boxed{P(x) - Q(x) = 2x^2 + 7x - 5}$$

---

### Question 14 (3 pts) — Expand `2x · (x + 3)`

Apply distributivity:

$$2x \cdot (x + 3) = 2x \cdot x + 2x \cdot 3 = \boxed{2x^2 + 6x}$$

---

### Question 15 (3 pts) — Expand `(x + 4)(x − 2)`

Apply the double-distributivity (FOIL):

$$(x+4)(x-2) = x \cdot x + x \cdot (-2) + 4 \cdot x + 4 \cdot (-2)$$

$$= x^2 - 2x + 4x - 8 = \boxed{x^2 + 2x - 8}$$

---

### Question 16 (3 pts) — Evaluate `P(2)` for `P(x) = x² − 3x + 5`

Substitute `x = 2`:

$$P(2) = 2^2 - 3 \cdot 2 + 5 = 4 - 6 + 5 = \boxed{3}$$

---

## Bonus (+3 pts)

Jacket costs **80 €**, reduced by **25 %**, then the new price increased by **25 %**.

**Step 1 — apply the 25 % reduction:**

$$80 \cdot \left(1 - \tfrac{25}{100}\right) = 80 \cdot 0.75 = 60 \text{ €}$$

**Step 2 — apply the 25 % increase to the reduced price:**

$$60 \cdot \left(1 + \tfrac{25}{100}\right) = 60 \cdot 1.25 = 75 \text{ €}$$

**Final price = 75 €**, **not** 80 €.

**Why?** Combining a `−25 %` then `+25 %` change multiplies by

$$0.75 \times 1.25 = 0.9375 < 1$$

i.e. a net loss of `6.25 %`. Equal percentage changes in opposite directions **do not cancel** because they are applied to *different* bases (first 80 €, then 60 €).
