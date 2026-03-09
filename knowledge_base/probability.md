# Probability for Agentic Systems

## 1. Introduction to Probability
Probability is a measure of how likely an event is to occur, calculated as the ratio of favorable outcomes to total possible outcomes.

**Basic Formula**:  
`P(Event) = Favourable Outcomes / Total Outcomes = x / n`

**Applications**: Predicting outcomes in coin tosses, dice rolls, card draws, and other random experiments.

---

## 2. Core Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Sample Point** | A single possible outcome. | Queen of clubs in a deck. |
| **Experiment/Trial** | A procedure with unpredictable results. | Tossing a coin, rolling a die. |
| **Random Experiment** | An action with uncertain outcomes. | Drawing a card from a shuffled deck. |
| **Sample Space (S)** | Set of all possible outcomes. | For a die: {1,2,3,4,5,6}. |
| **Favourable Outcomes** | Outcomes of interest for an event. | Getting an even number on a die. |
| **Event** | Subset of the sample space. | Rolling a prime number (2,3,5). |

### Event Classifications
- **Equally Likely Events**: Same probability of occurring (e.g., each face of a fair die).
- **Exhaustive Events**: At least one event must occur (e.g., die outcomes 1–6 cover all possibilities).
- **Mutually Exclusive Events**: Cannot occur simultaneously.  
  `P(A ∩ B) = 0`
- **Independent Events**: Occurrence of one does not affect the other.  
  `P(A ∩ B) = P(A) × P(B)`
- **Dependent Events**: Occurrence of one affects the probability of the other.
- **Complementary Event (A')**: Event A does **not** occur.  
  `P(A') = 1 - P(A)`
- **Impossible Event**: Cannot happen. `P(∅) = 0`
- **Sure Event**: Must happen. `P(S) = 1`

---

## 3. Mathematical Definition
For a sample space `S` with `n(S) = n` equally likely outcomes, and event `E` with `n(E) = m` favorable outcomes:

$$
P(E) = \frac{n(E)}{n(S)} = \frac{m}{n}
$$

**Properties**:
- `0 ≤ P(E) ≤ 1`
- `P(E) = 0` → Impossible event.
- `P(E) = 1` → Certain event.
- `P(E) + P(E') = 1`

---

## 4. Types of Probability

| Type | Basis | Example |
|------|-------|---------|
| **Theoretical** | Logic and known symmetries. | Coin toss: `P(Head) = 1/2`. |
| **Experimental** | Actual observations/experiments. | Toss coin 8 times, get 4 heads: `P(Head) = 4/8 = 0.5`. |
| **Axiomatic** | Kolmogorov's axioms (formal rules). | Quantifies existence/non-existence via axioms. |

---

## 5. Fundamental Formulas

### Addition Rule
For any events `A` and `B`:
$$
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
$$
- If `A` and `B` are mutually exclusive: `P(A ∪ B) = P(A) + P(B)`.

For three events `A, B, C`:
$$
P(A ∪ B ∪ C) = P(A) + P(B) + P(C) - P(A ∩ B) - P(B ∩ C) - P(A ∩ C) + P(A ∩ B ∩ C)
$$
- If mutually exclusive: `P(A ∪ B ∪ C) = P(A) + P(B) + P(C)`.

### Conditional Probability
Probability of `A` given `B` has occurred (`P(B) ≠ 0`):
$$
P(A|B) = \frac{P(A ∩ B)}{P(B)}
$$
Similarly, `P(B|A) = P(A ∩ B) / P(A)` (if `P(A) ≠ 0`).

**Multiplication Rule**:  
`P(A ∩ B) = P(A|B) × P(B) = P(B|A) × P(A)`

---

## 6. Key Theorems & Distributions

### Law of Total Probability
For mutually exclusive and exhaustive events `E₁, E₂, ..., Eₙ`:
$$
P(A) = \sum_{i=1}^{n} P(E_i) \times P(A|E_i)
$$

### Bayes' Theorem
For events `E₁, ..., Eₙ` (mutually exclusive, exhaustive) and `P(A) ≠ 0`:
$$
P(E_i|A) = \frac{P(E_i) \times P(A|E_i)}{\sum_{i=1}^{n} P(E_i) \times P(A|E_i)}
$$

### Binomial Distribution
For `n` independent trials, success probability `p`, failure `q = 1-p`:
$$
P(x) = \binom{n}{x} p^x q^{n-x}, \quad x = 0,1,...,n
$$
- **Mean**: `μ = np`
- **Variance**: `σ² = npq`
- **Standard Deviation**: `σ = √(npq)`

---

## 7. Common Scenarios & Quick Reference

### Coin Toss Probability
| Tosses | Outcomes | Example Probabilities |
|--------|----------|----------------------|
| 1 coin | {H, T} | `P(H)=1/2`, `P(T)=1/2` |
| 2 coins | 4 outcomes | `P(2H)=1/4`, `P(1H)=1/2`, `P(0H)=1/4` |
| 3 coins | 8 outcomes | `P(0H)=1/8`, `P(1H)=3/8`, `P(2H)=3/8`, `P(3H)=1/8` |

### Dice Roll Probability
- **One die**: Sample space `{1,2,3,4,5,6}`
  - `P(Even) = 3/6 = 1/2`
  - `P(Prime: 2,3,5) = 3/6 = 1/2`
- **Two dice**: Total outcomes = `6² = 36`
  - `P(doublet) = 6/36 = 1/6`
  - `P(sum=7) = 6/36 = 1/6`
  - `P(at least one 3) = 11/36`
- **n dice**: Total outcomes = `6ⁿ`

### Card Deck Probability (52 cards)
| Category | Count | Probability |
|----------|-------|-------------|
| Black cards (♣,♠) | 26 | `26/52 = 1/2` |
| Red cards (♥,♦) | 26 | `26/52 = 1/2` |
| Hearts | 13 | `13/52 = 1/4` |
| Face cards (J,Q,K) | 12 | `12/52 = 3/13` |
| Number 4 cards | 4 | `4/52 = 1/13` |
| Red 4 cards | 2 | `2/52 = 1/26` |

---

## 8. Probability Tree Diagrams
- Visual tool mapping all outcomes branching from a root.
- Probabilities on branches; sum of branches from any node = 1.
- Multiply probabilities along paths for joint events; sum for total probabilities.

---

## 9. Important Notes for Agentic Systems
- **Probability Range**: Always `0 ≤ P ≤ 1`.
- **Complementary Rule**: `P(A) + P(A') = 1`.
- **Impossible Event**: `P(∅) = 0`.
- **Sure Event**: `P(S) = 1`.
- **Comparison**: `P(A) > P(B)` ⇒ A more likely than B.
- **Pattern Recognition**: 
  - Use **addition rule** for "OR" scenarios (union).
  - Use **multiplication/conditional** for "AND" scenarios (intersection).
  - **Mutually exclusive** → no overlap; **independent** → no influence.
  - **Combinatorial problems** → count favorable/total using permutations/combinations.
  - **Repeated trials with two outcomes** → binomial distribution.

---

## 10. Solved Problem Patterns

### Example 1: Dice Sum Prime
**Problem**: Two dice thrown; find `P(sum is prime)`.  
**Pattern**: Count favorable `(a,b)` pairs in sample space `S` (size 36).  
**Solution**:  
- `S` size = 36.  
- Favorable pairs: 15.  
- `P = 15/36 = 5/12`.

### Example 2: Binomial Trial
**Problem**: Fair die rolled 4 times; `P(exactly 2 sixes)`.  
**Pattern**: Binomial with `n=4, x=2, p=1/6, q=5/6`.  
**Solution**:  
$$
P = \binom{4}{2} (1/6)^2 (5/6)^2 = 6 \times \frac{1}{36} \times \frac{25}{36} = \frac{150}{1296} = \frac{25}{216}
$$

### Example 3: Permutation with Restrictions
**Problem**: Arrange "PROBABILITY" with no adjacent vowels.  
**Pattern**: Arrange consonants first → place vowels in gaps.  
**Solution**:  
- Consonants (7, with 2 B's): `7!/2! = 2520` ways.  
- Gaps between consonants: 8 gaps. Choose 4 for vowels: `⁸C₄ = 70`.  
- Arrange vowels (4, with 2 I's): `4!/2! = 12`.  
- Total: `2520 × 70 × 12 = 2,116,800`.

### Example 4: Simple Favorable/Total
**Problem**: Bag with 3 red, 2 yellow marbles; `P(red)`.  
**Pattern**: Direct `favorable / total`.  
**Solution**:  
- Total marbles = 5.  
- `P(red) = 3/5`.

---

## 11. Quick Formula Sheet
| Concept | Formula |
|---------|---------|
| Basic Probability | `P(E) = n(E)/n(S)` |
| Complement | `P(A') = 1 - P(A)` |
| Conditional | `P(A|B) = P(A∩B)/P(B)` |
| Multiplication | `P(A∩B) = P(A|B)P(B)` |
| Addition (general) | `P(A∪B) = P(A)+P(B)-P(A∩B)` |
| Addition (mutually exclusive) | `P(A∪B) = P(A)+P(B)` |
| Binomial PMF | `P(x) = C(n,x) p^x q^(n-x)` |
| Binomial Mean | `μ = np` |
| Binomial Variance | `σ² = npq` |

---

## 12. Summary for Agentic Implementation
1. **Identify experiment type** (coin, dice, cards, binomial, etc.).
2. **Define sample space** `S` and event `E`.
3. **Check event relationships** (mutually exclusive? independent?).
4. **Apply appropriate formula**:
   - Simple ratio → `P = favorable/total`.
   - "OR" → addition rule.
   - "AND" → multiplication/conditional.
   - Repeated trials → binomial.
5. **For complex arrangements**:
   - Use permutations/combinations.
   - Handle restrictions (e.g., no two vowels together) via gap method.
6. **Validate**: `0 ≤ P ≤ 1`; `P(A)+P(A')=1`.

**Markdown Conversion Note**: This document uses standard markdown with LaTeX-style math for formula clarity. Sections are hierarchically structured (`#`, `##`, `###`) for easy parsing by RAG systems. Tables and lists optimize quick reference.