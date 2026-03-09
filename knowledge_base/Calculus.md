# Calculus for Agentic Problem-Solving: Limits & Derivatives

## 1. Introduction to Calculus
Calculus is the mathematical study of **change and motion**. Its two foundational pillars are:
- **Limits**: Describe how a function behaves as the input approaches a specific value.
- **Derivatives**: Measure the instantaneous rate of change (slope) of a function at any point.

**Core Purpose for Agentic Systems**: Enables automated reasoning about continuous change, optimization, and dynamic systems.

---

## 2. Limits of a Function

### 2.1 Conceptual Definition
The **limit** of a function \( f(x) \) as \( x \) approaches \( a \) is the value \( L \) that \( f(x) \) gets arbitrarily close to, regardless of whether \( f(a) \) is defined.

**Key Insight**: Limits describe behavior *near* a point, not *at* the point.

**Example**:  
For \( f(x) = x + 2 \),  
\[
\lim_{x \to 3} f(x) = 5
\]  
even if \( f(3) \) is undefined (as in a modified function \( g(x) \)).

### 2.2 Limit Representation
\[
\lim_{x \to a} f(x) = L
\]

### 2.3 Fundamental Theorems
| Theorem | Statement |
|---------|-----------|
| **Theorem 1** | If \( f \) is polynomial/rational and \( a \) is in its domain, then \( \lim_{x \to a} f(x) = f(a) \). |
| **Theorem 2** | If \( f(x) = g(x) \) for all \( x \neq a \), then \( \lim_{x \to a} f(x) = \lim_{x \to a} g(x) \). |

### 2.4 Properties of Limits
Given \( \lim_{x \to a} f(x) \) and \( \lim_{x \to a} g(x) \) exist, and \( c \) is constant:
\[
\begin{aligned}
\lim_{x \to a} [c \cdot f(x)] &= c \cdot \lim_{x \to a} f(x) \\
\lim_{x \to a} [f(x) \pm g(x)] &= \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x) \\
\lim_{x \to a} [f(x) \cdot g(x)] &= \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x) \\
\lim_{x \to a} \left[ \frac{f(x)}{g(x)} \right] &= \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}, \quad \text{if } \lim_{x \to a} g(x) \neq 0 \\
\lim_{x \to a} [f(x)]^n &= \left[ \lim_{x \to a} f(x) \right]^n, \quad n \in \mathbb{R} \\
\lim_{x \to a} \sqrt[n]{f(x)} &= \sqrt[n]{\lim_{x \to a} f(x)} \\
\lim_{x \to a} c &= c \\
\lim_{x \to a} x &= a \\
\lim_{x \to a} x^n &= a^n, \quad n \in \mathbb{Z}^+
\end{aligned}
\]

### 2.5 Essential Limit Formulas

#### Trigonometric Limits
\[
\begin{aligned}
\lim_{x \to 0} \sin(x) &= 0 \\
\lim_{x \to 0} \cos(x) &= 1 \\
\lim_{x \to 0} \frac{1 - \cos(x)}{x} &= 0 \\
\lim_{x \to 0} \frac{\sin^{-1}(x)}{x} &= 1 \\
\lim_{x \to 0} \frac{\tan^{-1}(x)}{x} &= 1 \\
\lim_{x \to 0} \frac{\sin(x)}{x} &= 1 \\
\lim_{x \to 0} \frac{\tan(x)}{x} &= 1 \\
\end{aligned}
\]

#### Exponential & Logarithmic Limits
\[
\begin{aligned}
\lim_{x \to 0} e^x &= 1 \\
\lim_{x \to 0} \frac{e^x - 1}{x} &= 1 \\
\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x &= e \\
\lim_{x \to \infty} \left(1 + \frac{a}{x}\right)^x &= e^a \\
\lim_{x \to 0} (1 + x)^{1/x} &= e \\
\lim_{x \to 0} \frac{a^x - 1}{x} &= \ln(a) \\
\lim_{x \to 0} \frac{\log(1 + x)}{x} &= 1 \\
\end{aligned}
\]

#### Polynomial Difference Quotient (Xn Formula)
\[
\lim_{x \to a} \frac{x^n - a^n}{x - a} = n \cdot a^{n-1}
\]

### 2.6 L’Hôpital’s Rule
For indeterminate forms \( \frac{0}{0} \) or \( \frac{\infty}{\infty} \):
\[
\text{If } \lim_{x \to a} f(x) = 0, \lim_{x \to a} g(x) = 0, \text{ then } \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
\]
provided the right-hand limit exists.

### 2.7 Existence Check: Two-Sided Limit
A limit \( \lim_{x \to a} f(x) \) exists **iff**:
\[
\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = f(a) \quad (\text{if } f(a) \text{ defined})
\]
- **Left-hand limit (LHL)**: \( x \) approaches \( a \) from below.
- **Right-hand limit (RHL)**: \( x \) approaches \( a \) from above.

---

## 3. Derivatives

### 3.1 Conceptual Definition
The **derivative** of \( f(x) \) at \( x \) is the instantaneous rate of change, defined as the limit of the difference quotient:
\[
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
\]

**Geometric Interpretation**: Slope of the tangent line to the curve at point \( (x, f(x)) \).

### 3.2 Derivative Representation
Common notations:
\[
f'(x), \quad \frac{df}{dx}, \quad \frac{d}{dx}[f(x)], \quad Df(x)
\]

### 3.3 Core Derivative Rules (Pattern Library)

| Rule | Formula | Example |
|------|---------|---------|
| **Power Rule** | \( \frac{d}{dx}[x^n] = n x^{n-1} \) | \( \frac{d}{dx}[x^3] = 3x^2 \) |
| **Constant Multiple** | \( \frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x) \) | \( \frac{d}{dx}[5x^2] = 10x \) |
| **Sum/Difference** | \( \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x) \) | \( \frac{d}{dx}[x^2 + x] = 2x + 1 \) |
| **Product Rule** | \( \frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x) \) | \( \frac{d}{dx}[x \cdot \sin x] = \sin x + x \cos x \) |
| **Quotient Rule** | \( \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2} \) | \( \frac{d}{dx}\left[\frac{x+1}{x}\right] = -\frac{1}{x^2} \) |
| **Chain Rule** | \( \frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x) \) | \( \frac{d}{dx}[\sin(x^2)] = 2x \cos(x^2) \) |

### 3.4 Derivatives of Common Functions
\[
\begin{aligned}
\frac{d}{dx}[c] &= 0 \\
\frac{d}{dx}[x] &= 1 \\
\frac{d}{dx}[\sin x] &= \cos x \\
\frac{d}{dx}[\cos x] &= -\sin x \\
\frac{d}{dx}[\tan x] &= \sec^2 x \\
\frac{d}{dx}[e^x] &= e^x \\
\frac{d}{dx}[\ln x] &= \frac{1}{x} \\
\frac{d}{dx}[\log_a x] &= \frac{1}{x \ln a} \\
\end{aligned}
\]

---

## 4. Applications for Agentic Systems

### 4.1 Applications of Limits
- **Indeterminate Form Resolution**: Evaluate \( \frac{0}{0}, \frac{\infty}{\infty} \) via L’Hôpital or algebraic manipulation.
- **Continuity Checking**: Verify \( \lim_{x \to a} f(x) = f(a) \).
- **Asymptotic Behavior**: Analyze \( \lim_{x \to \infty} f(x) \) for end behavior.
- **Infinitesimal Approximations**: Model physics at quantum/relativistic scales.

### 4.2 Applications of Derivatives
- **Optimization**: Find maxima/minima via \( f'(x) = 0 \) and second derivative test.
- **Motion Analysis**:  
  - Velocity \( v(t) = s'(t) \)  
  - Acceleration \( a(t) = v'(t) = s''(t) \)
- **Marginal Analysis** (Economics):  
  - Marginal Cost \( MC = C'(q) \)  
  - Marginal Revenue \( MR = R'(q) \)
- **Curve Sketching**: Determine increasing/decreasing intervals, concavity, inflection points.
- **Elasticity**: \( E = \frac{d \ln Q}{d \ln P} \)

---

## 5. Solved Examples (Pattern Recognition Templates)

### Example 1: Limit Evaluation (Algebraic Simplification)
**Problem**: \( \lim_{x \to 3} \frac{x^2 - 9}{x - 3} \)

**Solution Pattern** (Indeterminate \( \frac{0}{0} \)):
1. Factor numerator: \( x^2 - 9 = (x+3)(x-3) \)
2. Cancel common term: \( \frac{(x+3)\cancel{(x-3)}}{\cancel{x-3}} \)
3. Substitute: \( \lim_{x \to 3} (x+3) = 6 \)

**Result**: \( 6 \)

---

### Example 2: Derivative Using Quotient Rule
**Problem**: \( f(x) = \frac{x+1}{x} \)

**Solution Pattern** (Quotient Rule \( \left( \frac{u}{v} \right)' = \frac{u'v - uv'}{v^2} \)):
1. Let \( u = x+1 \), \( v = x \)
2. Compute: \( u' = 1 \), \( v' = 1 \)
3. Apply: \( f'(x) = \frac{(1)(x) - (x+1)(1)}{x^2} = \frac{x - x - 1}{x^2} = -\frac{1}{x^2} \)

**Result**: \( f'(x) = -\frac{1}{x^2} \)

---

### Example 3: Trigonometric Limit with L’Hôpital
**Problem**: \( \lim_{x \to 0} \frac{\sin(4x)}{\tan(x)} \)

**Solution Pattern** (Indeterminate \( \frac{0}{0} \)):
1. Recognize standard limit: \( \lim_{x \to 0} \frac{\sin(kx)}{kx} = 1 \)
2. Multiply/divide by \( 4x \):
   \[
   \lim_{x \to 0} \left( \frac{\sin(4x)}{4x} \cdot \frac{4x}{\tan x} \right)
   \]
3. Split: \( \left( \lim_{x \to 0} \frac{\sin(4x)}{4x} \right) \cdot \left( 4 \lim_{x \to 0} \frac{x}{\tan x} \right) \)
4. Use \( \lim_{x \to 0} \frac{x}{\tan x} = 1 \) (since \( \tan x \sim x \))
5. Compute: \( 1 \times 4 \times 1 = 4 \)

**Result**: \( 4 \)

---

### Example 4: Polynomial Derivative (Power Rule)
**Problem**: \( f(x) = 2x^2 + 3x - 4 \)

**Solution Pattern** (Linear combination of power functions):
1. Apply sum rule: \( f'(x) = \frac{d}{dx}(2x^2) + \frac{d}{dx}(3x) - \frac{d}{dx}(4) \)
2. Use constant multiple & power rule:
   \[
   = 2 \cdot 2x + 3 \cdot 1 - 0
   \]
3. Simplify: \( 4x + 3 \)

**Result**: \( f'(x) = 4x + 3 \)

---

## 6. Agentic System Implementation Notes

### Key Patterns for Automated Problem-Solving:
1. **Limit Classification**:
   - Direct substitution → evaluate.
   - Indeterminate form → factor/simplify or L’Hôpital.
   - Trigonometric → use standard limits.
   - Exponential → use \( e \)-related identities.

2. **Derivative Rule Selection**:
   - Single term → power rule.
   - Product of functions → product rule.
   - Quotient → quotient rule.
   - Composition → chain rule.

3. **Verification Steps**:
   - Check domain restrictions.
   - Validate indeterminate forms before L’Hôpital.
   - For derivatives, confirm by simplifying or numerical check.

### LaTeX Formatting for RAG:
- Use `\( ... \)` for inline math.
- Use `$$ ... $$` for displayed equations.
- Store formulas as key-value pairs in knowledge base:
  ```json
  {
    "formula": "\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1",
    "category": "trig_limit",
    "pattern": "sinc_normalization"
  }
  ```

---

*Prepared for RAG-based Agentic Calculus Solver*  
*Senior Data Scientist — Knowledge Structuring for Automated Reasoning*