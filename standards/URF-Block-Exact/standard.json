{
  "standard": "URF-Block-Exact",
  "version": "1.1",
  "status": "binding-core-standard",
  "scope": "All rigidity / stability / robustness claims in URF",

  "purpose": "Replace informal perturbative stability claims with a single block-exact operator criterion.",

  "formal_definition": {
    "objects": {
      "H": "Hilbert space",
      "A": "Self-adjoint operator with compact resolvent",
      "V": "Symmetric A-bounded perturbation",
      "Ek": "Eigenspace of lambda_k",
      "Ek1": "Eigenspace of lambda_{k+1}"
    },
    "projection": "Pi = projection onto Ek ⊕ Ek1",
    "criterion": "Pi V Pi == 0"
  },

  "allowed_claims": [
    {
      "type": "rigid",
      "condition": "Pi V Pi == 0",
      "consequence": "|gamma_k(eps) - gamma_k(0)| = O(eps^2)"
    },
    {
      "type": "generic-non-rigid",
      "condition": "Pi V Pi != 0",
      "consequence": "|gamma_k(eps) - gamma_k(0)| = Theta(|eps|)"
    }
  ],

  "prohibited_language": [
    "stable",
    "robust",
    "protected",
    "insensitive",
    "rigid under perturbations"
  ],

  "mechanical_verification": {
    "tool": "tools/block_exact_check.py",
    "command": "python tools/block_exact_check.py A.json V.json k",
    "output_field": "block_exact_rigid"
  },

  "finite_witnesses": [
    {
      "operator": "tools/A_s1_trunc8.json",
      "perturbation": "tools/V_s1_rigid.json",
      "result": "Pi V Pi = 0"
    },
    {
      "operator": "tools/A_s1_trunc8.json",
      "perturbation": "tools/V_s1_break.json",
      "result": "Pi V Pi != 0"
    }
  ],

  "audit_binding": {
    "ledger": "URF-AUDIT.md",
    "requirement": "Every rigidity claim must appear with computed Pi V Pi."
  },

  "conceptual_statement": "All URF rigidity reduces to the invariant Pi V Pi. No other stability principle exists.",

  "research_frontier": [
    "Classification of admissible perturbations V",
    "Symmetry forcing of block invariance",
    "Representation-theoretic obstructions to Pi V Pi != 0"
  ]
}

