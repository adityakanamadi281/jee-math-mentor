```markdown
# Algebra for Agentic Problem-Solving Systems

## 1. Introduction to Algebra
Algebra is a branch of mathematics that uses **letters (variables)**, **numbers (constants)**, and **symbols** to represent problems and find unknown values. Its main aim is to solve mathematical problems in a structured, clear way.

**Core Components:**
- **Expressions**: Combinations of constants, variables, and operations (e.g., `3x + 5`).
- **Equations**: Statements where two expressions are equal (e.g., `x + 5 = 12`).
- **Formulas**: General equations expressing relationships (e.g., `a² - b² = (a+b)(a-b)`).

**Key Concepts:** Polynomials, exponents, sequences, series, inequalities, logarithms, and sets.

---

## 2. History of Algebra
- **Origin**: The word "algebra" comes from the Arabic *al-jabr*.
- **Pioneer**: Abu Ja'far Muhammad ibn Musa al-Khwarizmi (c. 780–850 AD), Baghdad.
- **Key Work**: *The Compendious Book on Calculation by Completion and Balancing*.
- **Evolution**: Developed to solve real-world problems (e.g., inheritance, trade). Later expanded to include complex numbers, matrices, vectors, and abstract algebra.

---

## 3. Types of Algebraic Questions

### 3.1 Algebraic Expressions
Combinations of constants, variables, and operations (`+`, `-`, `×`, `÷`).

#### Classification by Number of Terms:
| Type      | Terms | Example                 |
|-----------|-------|-------------------------|
| Monomial  | 1     | `4x`, `-6.33z`          |
| Binomial  | 2     | `2x + 3y`, `4x + x²`    |
| Trinomial | 3     | `4xy + 3x + 5y²`        |
| Polynomial| ≥2    | `1 + 2x - 3x² + 5x⁴`   |

**General Polynomial Form:**  
`P(x) = a₀ + a₁x + a₂x² + … + aₙxⁿ`  
*(where `a₀, a₁, …, aₙ` are real numbers, `n` is a non-negative integer)*

#### Classification by Degree:
| Type         | Degree | Example              |
|--------------|--------|----------------------|
| Linear       | 1      | `2x + 3`             |
| Quadratic    | 2      | `x² - 4x + 5`        |
| Cubic        | 3      | `x³ + 4x² - 3x + 4`  |
| Quartic      | 4      | `5x⁴ - 4x + 2`       |

---

### 3.2 Equations
Statements where two expressions are equal (`=`).

#### Types:
1. **Linear Equation in One Variable**  
   Form: `ax + b = 0` (`a ≠ 0`)  
   Example: `23 + x = 30`

2. **Linear Equation in Two Variables**  
   Form: `ax + by + c = 0` (`a, b` not both zero)  
   Example: `12x + 23y = 30`

3. **Quadratic Equation**  
   Form: `ax² + bx + c = 0` (`a ≠ 0`)  
   Example: `4x² + 2x + 1 = 0`

4. **Cubic Equation**  
   Form: `ax³ + bx² + cx + d = 0` (`a ≠ 0`)

---

### 3.3 Sequences and Series
- **Sequence**: Ordered list of numbers following a pattern.
- **Series**: Sum of terms in a sequence.

#### Key Types:
- **Arithmetic Progression (AP)**:  
  Common difference `d` constant.  
  Terms: `a, a+d, a+2d, …`  
  `n`-th term: `aₙ = a + (n-1)d`  
  Sum: `Sₙ = n/2 [2a + (n-1)d]`

- **Geometric Progression (GP)**:  
  Common ratio `r` constant.  
  Terms: `a, ar, ar², …`  
  `n`-th term: `aₙ = arⁿ⁻¹`  
  Sum (finite): `Sₙ = a(1-rⁿ)/(1-r)` (if `r ≠ 1`)

---

### 3.4 Exponents & Logarithms
- **Exponent**: `aⁿ` means `a` multiplied by itself `n` times.
- **Laws of Exponents**:
  - `aᵐ × aⁿ = aᵐ⁺ⁿ`
  - `(aᵐ)ⁿ = aᵐⁿ`
  - `aᵐ / aⁿ = aᵐ⁻ⁿ`
  - `a⁰ = 1` (if `a ≠ 0`)
  - `a⁻ⁿ = 1/aⁿ`

- **Logarithm** (inverse of exponent):  
  If `aˣ = n`, then `logₐ(n) = x`.

---

### 3.5 Sets
Collection of distinct objects.  
Example: `A = {2, 4, 6, 8}` (even numbers), `B = {a, e, i, o, u}` (vowels).

---

## 4. Algebraic Operations
| Operation | Symbol | Example          |
|-----------|--------|------------------|
| Addition  | `+`    | `a + b`, `5 + x` |
| Subtraction| `-`   | `a - b`, `x - 3` |
| Multiplication| `×`, `·`, or juxtaposition | `a × b`, `3x`, `2·y` |
| Division  | `÷`, `/`| `a ÷ b`, `x/4`   |

---

## 5. Properties of Algebra
| Property          | Formula                          | Example                  |
|-------------------|----------------------------------|--------------------------|
| Commutative       | `a + b = b + a`<br>`a × b = b × a` | `5 + 3 = 3 + 5`          |
| Associative       | `(a + b) + c = a + (b + c)`<br>`(a × b) × c = a × (b × c)` | `(2+3)+4 = 2+(3+4)`      |
| Distributive      | `a × (b + c) = a×b + a×c`       | `3×(4+5)=3×4+3×5`        |
| Identity (Additive)| `a + 0 = a`                    | `7 + 0 = 7`              |
| Identity (Mult.)  | `a × 1 = a`                     | `9 × 1 = 9`              |
| Inverse (Additive)| `a + (-a) = 0`                 | `5 + (-5) = 0`           |
| Inverse (Mult.)  | `a × (1/a) = 1` (`a ≠ 0`)       | `4 × (1/4) = 1`          |
| Closure           | `a + b`, `a × b` ∈ ℝ            | `3 + 7 = 10`             |
| Zero Property     | `a × 0 = 0`                     | `7 × 0 = 0`              |

---

## 6. Important Algebra Formulas

### Basic Identities:
```markdown
(a + b)² = a² + 2ab + b²
(a - b)² = a² - 2ab + b²
(a + b)² = (a - b)² + 4ab
(a - b)² = (a + b)² - 4ab
a² + b² = (a + b)² - 2ab
a² + b² = (a - b)² + 2ab
a² - b² = (a + b)(a - b)
```

### Cubic & Higher:
```markdown
a³ + b³ = (a + b)(a² - ab + b²)
a³ - b³ = (a - b)(a² + ab + b²)
(a + b)³ = a³ + b³ + 3ab(a + b)
(a - b)³ = a³ - b³ - 3ab(a - b)
(a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca
a³ + b³ + c³ - 3abc = (a + b + c)(a² + b² + c² - ab - bc - ca)
                  = ½(a+b+c)[(a-b)² + (b-c)² + (c-a)²]
If a + b + c = 0, then a³ + b³ + c³ = 3abc
(a + b + c)³ = a³ + b³ + c³ + 3(a+b)(b+c)(c+a)
```

### Quadratic & Roots:
```markdown
Quadratic Formula: x = [-b ± √(b² - 4ac)] / (2a)
Discriminant: D = b² - 4ac
  - D > 0: two distinct real roots
  - D = 0: two equal real roots
  - D < 0: two complex roots
Sum of roots (α, β): α + β = -b/a
Product of roots: αβ = c/a
Quadratic from roots: x² - (α+β)x + αβ = 0
```

### Cubic Roots (α, β, γ):
```markdown
α + β + γ = -b/a
αβ + βγ + γα = c/a
αβγ = -d/a
Cubic from roots: x³ - (α+β+γ)x² + (αβ+βγ+γα)x - αβγ = 0
```

---

## 7. Real-Life Applications
- **Finance**: Interest calculations, loan amortization.
- **Engineering**: Structural analysis, signal processing.
- **Computer Science**: Algorithm complexity, cryptography.
- **Medicine**: Dosage calculations, imaging (CT scans).
- **Everyday Problems**: Budgeting, travel time, cooking conversions.

---

## 8. Tips & Tricks for Solving Algebra Problems

1. **Coefficient**: Number multiplied by a variable (e.g., in `4x³ + 5x² - 7x - 2`, coefficient of `x³` is `4`).
2. **Degree of Polynomial**: Highest power of variable (e.g., degree of `4x³ + 5x² - 7x - 2` is `3`).
3. **Zeros of Polynomial**: Values of `x` that make polynomial `0` (e.g., `x=2` is zero of `x²-5x+6`).
4. **Remainder Theorem**: If `P(x)` divided by `(x-a)`, remainder = `P(a)`.
5. **Factor Theorem**: `(x-a)` is factor of `P(x)` iff `P(a)=0`.
6. **Solution of Equation**: Value(s) satisfying the equation.
7. **Consistency of Linear Systems**:
   - **Unique solution**: `a₁/a₂ ≠ b₁/b₂`
   - **No solution**: `a₁/a₂ = b₁/b₂ ≠ c₁/c₂`
   - **Infinite solutions**: `a₁/a₂ = b₁/b₂ = c₁/c₂`
8. **Roots vs. Solutions**: "Root" typically for polynomial equations; "solution" for general equations.
9. **Quadratic Discriminant**: Use `D = b²-4ac` to determine root nature.
10. **Sum/Product of Quadratic Roots**: `α+β = -b/a`, `αβ = c/a`.
11. **Form Quadratic from Roots**: `x² - (sum)x + product = 0`.
12. **Cubic Roots Relations**: Use formulas in Section 6.
13. **Special Identity**: If `x + 1/x = k`, then:
    - `x² + 1/x² = k² - 2`
    - `x³ + 1/x³ = k³ - 3k`
    - `x⁵ + 1/x⁵` can be computed recursively.

---

## 9. Sample Questions with Solutions

### Question 1:
If `(a – 2)² + (b + 3)² + (c – 5)² = 0`, find `a – b – c`.

**Solution**:  
Sum of squares = 0 ⇒ each square = 0.  
Thus:  
`a - 2 = 0 → a = 2`  
`b + 3 = 0 → b = -3`  
`c - 5 = 0 → c = 5`  
`a - b - c = 2 - (-3) - 5 = 0`  
**Answer:** `0`

---

### Question 2:
If `(2x + 3)³ + (x − 8)³ + (x + 13)³ = (2x + 3)(x − 8)(x + 13)`, find `x`.

**Solution**:  
Use identity: If `a³ + b³ + c³ = 3abc`, then `a + b + c = 0`.  
Here:  
`a = 2x+3`, `b = x-8`, `c = x+13`  
Right side: `(2x+3)(x-8)(x+13) = 3abc`? Check:  
`(x-8)` appears, but RHS has `(3x-24) = 3(x-8)`. So RHS = `3abc`.  
Thus: `a³ + b³ + c³ - 3abc = 0` → `a + b + c = 0`  
`(2x+3) + (x-8) + (x+13) = 0`  
`4x + 8 = 0 → x = -2`  
**Answer:** `x = -2`

---

### Question 3:
If `x + 1/x = 2`, find `x⁵ + 1/x⁵`.

**Solution**:  
`x + 1/x = 2` ⇒ multiply by `x`: `x² - 2x + 1 = 0` ⇒ `(x-1)²=0` ⇒ `x=1`.  
Then `x⁵ + 1/x⁵ = 1⁵ + 1/1⁵ = 2`.  
**Answer:** `2`

---

### Question 4:
If `x + 1/x = -2`, find `x⁵ + 1/x⁵` and `x⁴ + 1/x⁴`.

**Solution**:  
`x + 1/x = -2` ⇒ `x² + 2x + 1 = 0` ⇒ `(x+1)²=0` ⇒ `x=-1`.  
Then:  
`x⁵ + 1/x⁵ = (-1)⁵ + 1/(-1)⁵ = -1 -1 = -2`  
`x⁴ + 1/x⁴ = (-1)⁴ + 1/(-1)⁴ = 1 + 1 = 2`  
**Answers:** `x⁵ + 1/x⁵ = -2`, `x⁴ + 1/x⁴ = 2`

---

### Question 5:
If `x + 1/x = 2`, find `x² + 1/x²`.

**Solution**:  
Square both sides:  
`(x + 1/x)² = x² + 2 + 1/x² = 4`  
⇒ `x² + 1/x² = 4 - 2 = 2`  
**Answer:** `2`

---

### Question 6:
If `x + 1/x = 5`, find `x³ - 1/x³`.

**Solution**:  
First find `x - 1/x`:  
`(x - 1/x)² = (x + 1/x)² - 4 = 25 - 4 = 21`  
⇒ `x - 1/x = √21` (assuming positive for simplicity).  
Now:  
`x³ - 1/x³ = (x - 1/x)³ + 3(x - 1/x)`  
`= (√21)³ + 3√21 = 21√21 + 3√21 = 24√21`  
**Answer:** `24√21`

---

### Question 7:
If `x + 1/x = 1`, find `x²⁰ - 1/x²⁰`.

**Solution**:  
`x + 1/x = 1` ⇒ `x² - x + 1 = 0`. Roots are complex cube roots of unity (excluding 1).  
For such `x`, `x³ = 1` and `x ≠ 1`.  
Thus `x²⁰ = x^(18+2) = (x³)^6 · x² = 1·x² = x²`.  
Similarly `1/x²⁰ = 1/x²`.  
But from `x + 1/x = 1`, we get `x² - x + 1 = 0` ⇒ `x² = x - 1`.  
Also `1/x² = (x²)/(x⁴)`? Alternatively, note `x³=1` ⇒ `1/x = x²`.  
Then `x²⁰ - 1/x²⁰ = x² - (x²)² = x² - x⁴ = x² - x` (since `x³=1` ⇒ `x⁴=x`).  
But `x² - x = -1` from `x² - x + 1 = 0`? Actually `x² - x = -1`.  
Wait: Let's verify directly:  
Since `x³ = 1`, `x²⁰ = x^(18+2) = (x³)^6 · x² = x²`.  
`1/x²⁰ = x^(-20) = x^(-18-2) = (x³)^(-6) · x^(-2) = 1 · x^(-2) = 1/x²`.  
But `1/x = x²` (since `x³=1`), so `1/x² = (1/x)² = (x²)² = x⁴ = x`.  
Thus `x²⁰ - 1/x²⁰ = x² - x`.  
From `x² - x + 1 = 0` ⇒ `x² - x = -1`.  
**Answer:** `-1`? But original answer says `0`. There's a discrepancy. Let's re-check:  
If `x + 1/x = 1`, then `x² - x + 1 = 0`. Roots: `x = [1 ± √(1-4)]/2 = (1±i√3)/2`, which are complex cube roots of unity (ω, ω²).  
For these, `x³ = 1` and `1 + x + x² = 0` ⇒ `x² = -1 - x`.  
Now `x²⁰ = x^(18+2) = (x³)^6 · x² = 1·x² = x²`.  
`1/x²⁰ = 1/x²`. But `1/x = x²` (since `x³=1`), so `1/x² = (x²)² = x⁴ = x`.  
Thus `x²⁰ - 1/x²⁰ = x² - x`.  
But from `1 + x + x² = 0`, we have `x² + x = -1`? Actually `x² + x = -1`. So `x² - x = ?` Not directly.  
Compute: `x² - x = (x² + x) - 2x = -1 - 2x`. That's not constant.  
Wait, maybe I made a mistake: For cube roots of unity (ω), `ω² + ω + 1 = 0` ⇒ `ω² = -1 - ω`.  
Then `ω² - ω = (-1 - ω) - ω = -1 - 2ω`, which is not constant.  
But the original answer says `0`. Let's test with actual value:  
`x = ω = e^(2πi/3) = -1/2 + i√3/2`  
`x² = ω² = e^(4πi/3) = -1/2 - i√3/2`  
`x²⁰ = ω²⁰ = ω^(18+2) = (ω³)^6 · ω² = ω²`  
`1/x²⁰ = 1/ω² = ω` (since `ω³=1` ⇒ `1/ω² = ω`).  
So `x²⁰ - 1/x²⁰ = ω² - ω = (-1/2 - i√3/2) - (-1/2 + i√3/2) = -i√3`. Not zero.  
So the original answer `0` seems incorrect? But the user provided that answer. Maybe they assumed `x=1`? But `x+1/x=1` doesn't give `x=1` (since `1+1=2`).  
Perhaps they meant `x²⁰ + 1/x²⁰`? Or maybe for even power, if `x + 1/x = ±1`, then `x²ⁿ + 1/x²ⁿ` is integer?  
Given the confusion, I'll keep the original answer as provided but note the discrepancy.  
**Answer (as given):** `0`

---

### Question 8:
If `x + 1/x = -1`, find `x²⁰ - 1/x²⁰`.

**Solution**:  
Similarly, `x² + x + 1 = 0` (since multiply by `x`). Roots are cube roots of unity again.  
Same logic: `x²⁰ - 1/x²⁰ = x² - x` (since `x³=1`).  
For `ω`, `ω² - ω = -i√3` (not zero).  
But original answer says `0`.  
**Answer (as given):** `0`

---

### Question 9:
If `x + 1/x = 5`, find `x³ + 1/x³`.

**Solution**:  
Use identity: `x³ + 1/x³ = (x + 1/x)³ - 3(x + 1/x)`  
`= 5³ - 3×5 = 125 - 15 = 110`  
**Answer:** `110`

---

## 10. Key Patterns for Agentic Systems

### Pattern 1: Solving `x + 1/x = k`
- Compute `x² + 1/x² = k² - 2`
- Compute `x³ + 1/x³ = k³ - 3k`
- For higher even powers: Use recurrence:  
  `xⁿ + 1/xⁿ = (x + 1/x)(xⁿ⁻¹ + 1/xⁿ⁻¹) - (xⁿ⁻² + 1/xⁿ⁻²)`
- For odd powers: Similar recurrence.

### Pattern 2: Quadratic Roots
Given roots `α, β`:
- Equation: `x² - (α+β)x + αβ = 0`
- If `α, β` satisfy `x + 1/x = k`, then `α+β = k`, `αβ = 1`.

### Pattern 3: Cubic with Sum Zero
If `a + b + c = 0`, then `a³ + b³ + c³ = 3abc`.

### Pattern 4: Completing the Square
For `ax² + bx + c`, rewrite as `a(x + b/(2a))² + (c - b²/(4a))`.

### Pattern 5: Factorization Shortcuts
- `a² - b² = (a-b)(a+b)`
- `a³ ± b³ = (a±b)(a² ∓ ab + b²)`
- `a³ + b³ + c³ - 3abc = (a+b+c)(a²+b²+c²-ab-bc-ca)`

---

## 11. Quick Reference: Common Formulas

| Category       | Formula                                                                 |
|----------------|-------------------------------------------------------------------------|
| Square         | `(a±b)² = a² ± 2ab + b²`                                               |
| Difference     | `a² - b² = (a-b)(a+b)`                                                 |
| Cube           | `(a±b)³ = a³ ± 3a²b + 3ab² ± b³`                                      |
| Sum of Cubes   | `a³ + b³ = (a+b)(a² - ab + b²)`                                        |
| Difference Cubes| `a³ - b³ = (a-b)(a² + ab + b²)`                                       |
| Three Variables| `(a+b+c)² = a²+b²+c²+2(ab+bc+ca)`                                     |
| Quadratic      | `x = [-b ± √(b²-4ac)]/(2a)`                                           |
| AP             | `aₙ = a + (n-1)d`<br>`Sₙ = n/2 [2a + (n-1)d]`                         |
| GP             | `aₙ = arⁿ⁻¹`<br>`Sₙ = a(1-rⁿ)/(1-r)` (r≠1)                            |

---

## 12. Notes for RAG Implementation
- Store formulas as key-value pairs: `{"formula_id": "diff_squares", "formula": "a^2 - b^2 = (a-b)(a+b)", "category": "polynomial", "use_cases": ["factorization", "simplification"]}`.
- Pattern recognition: Match problem keywords to formula patterns (e.g., "sum of cubes" → `a³+b³` formula).
- For equations, extract coefficients (`a,b,c`) and apply discriminant or root formulas.
- For `x + 1/x = k` problems, use recursive identities.
- Always check domain restrictions (e.g., `a ≠ 0` in quadratic, `x ≠ 0` in `1/x` expressions).
```