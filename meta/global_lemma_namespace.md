Global URF Lemma Namespace (Collision-Free)

Canonical Global Key

Let:
repoID        := globally unique repository identifier
modulePath    := canonical Lean module path
lemmaName     := Lean lemma identifier
H_L           := canonical lemma hash

Define global lemma key:
K_global(L) := repoID || modulePath || lemmaName || H_L

Collision Safety

Assumptions:
1. repoID unique across URF federation
2. modulePath canonicalized
3. lemmaName unique inside module
4. H_L collision resistant

Then K_global is collision-free except negligible probability.

Cross-Repo Federation Rule

Global DAG node identity is K_global(L).
Imports must reference K_global, not local names.

Rename Safety

Renaming module or lemma changes namespace portion but preserves H_L,
allowing equivalence tracking via H_L layer.

Deprecation Rule

If lemma is superseded:
- keep old K_global node
- add supersedes edge in DAG
