Title: AC0-Local CSP Class

Definition:
An AC0-local CSP is a constraint satisfaction problem where:
- Constraints have bounded arity
- Constraint scopes form a bounded-degree hypergraph
- Propagation rules are computable by AC0 circuits
- No global aggregation, counting, or linear algebra is allowed

Examples:
- Bounded-width CSPs
- Horn-SAT
- 2-SAT
- Fixed-template CSPs of bounded relational width

Model:
Solvers operate via iterative local propagation
with AC0 bounded-arity updates.

