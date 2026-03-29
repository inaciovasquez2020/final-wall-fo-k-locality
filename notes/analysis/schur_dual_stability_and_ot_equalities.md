Schur-dual stability

Let B be normal on ℂⁿ, ‖E‖ ≤ η, and B′ = B + E. For the dual constraint set

F(B) := { λ : ‖Bᵀ λ‖∞ ≤ w },

assume Bᵀ is injective on the relevant subspace and admits a bounded right-inverse R with ‖R‖ ≤ γ. Then

d_H(F(B), F(B′)) ≤ w γ² η + O(η²),

via

‖B′ᵀ λ‖∞ ≤ ‖Bᵀ λ‖∞ + ‖Eᵀ‖ ‖λ‖

and

‖λ‖ ≤ γ ‖Bᵀ λ‖

(normal B gives γ = 1/σ_min(Bᵀ) on the active subspace).

For the strongly concave quadratic dual objective

Φ(λ) = −bᵀ λ − (1/(2ρ)) ‖λ‖²,

the optimizer map satisfies

‖λ*(B) − λ*(B′)‖ ≤ ρ d_H(F(B), F(B′)) ≤ ρ w γ² η + O(η²).

Equality example for p ≠ 2

Let μ = N(m₀, Σ), ν = N(m₁, Σ). For any p ≥ 1,

W_p(μ, ν) = ‖m₀ − m₁‖

because the coupling X ∼ μ, Y = X + (m₁ − m₀) yields cost ‖m₁ − m₀‖^p and is optimal by translation invariance of W_p. Hence for

ρ(μ) = ∫ ⟨a, x⟩ dμ = ⟨a, m⟩,

|ρ(μ) − ρ(ν)| = |⟨a, m₀ − m₁⟩| ≤ ‖a‖ W_p(μ, ν),

with equality iff a ∥ (m₀ − m₁).

Second equality example

Let μ = N(0, σ₀²), ν = N(0, σ₁²) with d = 1. Then

W₂(μ, ν) = |σ₀ − σ₁|.

Quadratic risk

ρ(μ) = ∫ x² dμ = σ₀²,
ρ(ν) = σ₁².

Hence

|ρ(μ) − ρ(ν)|
= |σ₀² − σ₁²|
= (σ₀ + σ₁) |σ₀ − σ₁|
= (σ₀ + σ₁) W₂(μ, ν),

so the sharp constant for this pair is L = σ₀ + σ₁, and equality holds.
