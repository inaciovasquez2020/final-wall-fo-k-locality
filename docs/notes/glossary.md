---
title: URF Glossary
status: explanatory
scope: terminology / reference
---

**finite**  
A system is finite if it operates under a fixed upper bound on transcript capacity per step. In URF, finiteness refers to bounded information-processing capacity, not to the size of the object being studied.

**capacity**  
The maximum amount of information (entropy) that a refinement step can introduce, store, or resolve. Finite capacity is the core admissibility constraint of URF.

**transcript**  
The internal record of information accumulated by a refinement process. Bounds on transcript growth enforce capacity limits.

**admissible**  
A process is admissible if it respects all URF constraints, including locality and finite transcript capacity. Results in URF apply only to admissible processes.

**refinement**  
A stepwise process that reduces uncertainty by locally updating information. Refinement is sequential and capacity-bounded in URF.

**entropy demand**  
The total amount of uncertainty that must be resolved to complete a task or characterize an object. Denoted \(H(P)\).

**entropy depth**  
The minimum number of refinement steps required to resolve the entropy demand under capacity constraints. Denoted \(\mathrm{ED}(P)\).

**VCDI (Vasquez Capacity–Depth Inequality)**  
The inequality \(\mathrm{ED}(P) \ge H(P)/C_{\max}\), relating entropy demand to entropy depth under finite capacity.

**locality**  
The restriction that refinement steps can depend only on bounded-radius, bounded-width information. FO\(^k\) locality is the canonical formalization.

**global invariant**  
A quantity that cannot be computed or approximated using purely local refinement (e.g., cycle rank, global homology, spectral data). Use of global invariants violates URF locality.

**rigidity**  
The condition where a refinement process cannot terminate or converge within admissibility constraints, typically because entropy depth diverges.

**wall**  
A proven boundary beyond which admissible refinement cannot proceed. Walls separate feasible refinement from rigidity.

**infinity (URF context)**  
A regime characterized by unbounded entropy demand or unbounded capacity. Infinite objects are treated via finite exhaustions; direct refinement is rigid unless admissibility is violated.

**normalization**  
The choice of scale or unit in a setting without a natural bound. In infinite-capacity regimes, notions like time or steps reduce to normalization choices.

**bounded degree**  
A restriction that the underlying structure (e.g., a graph) has a uniform upper bound on local connectivity. Used to ensure finiteness of local types and enforce locality.

**FO^k locality**  
First-order logic with a fixed number of variables \(k\). FO^k locality formalizes the notion that only bounded, local neighborhoods can be inspected at each refinement step.

**exhaustion**  
A sequence of finite instances \((P_n)\) whose union or limit represents an infinite object. URF analyzes infinite objects only through such finite exhaustions.

**directed limit**  
The limiting object obtained from a directed system of finite instances. In URF, divergence of entropy depth along the system implies rigidity of the limit.

**capacity violation**  
Any mechanism by which unbounded information is injected or resolved in a single step. Capacity violation renders a process non-admissible.

**locality violation**  
Any mechanism that depends on non-local or global aggregation. Locality violation places a process outside the URF regime.

**global aggregation**  
Computation that requires combining information from unboundedly many locations. Global aggregation is forbidden in admissible refinement.

**termination**  
The event that a refinement process fully resolves its entropy demand in finitely many steps. Under URF, termination is possible only when entropy depth is finite.

**collapse**  
The phenomenon where distinct configurations or uncertainties become indistinguishable under bounded refinement. Collapse is often the mechanism behind rigidity.

**sharp bound**  
A lower or upper bound that cannot be improved within a fixed admissible class. VCDI is sharp with respect to the capacity constant.

**normal form**  
A canonical representation of a process or argument that makes capacity and locality constraints explicit.

**regime**  
A class of processes defined by shared structural constraints (e.g., admissible refinement regime vs. global-invariant regime).

**configuration**  
A local state or pattern visible to a bounded-radius, bounded-width observer. Configuration types are finite under bounded degree and fixed locality.

**configuration type**  
An equivalence class of configurations indistinguishable by FO^k-local refinement. Finite in number for fixed parameters.

**pumping**  
A normalization principle asserting that repeated visitation of the same configuration type yields a bounded local witness. Used to derive rigidity and walls.

**support**  
The minimal region on which a refinement step or witness depends. Bounded support is required for admissibility.

**support rigidity**  
The principle that bounded-support operations cannot generate unbounded global structure without violating capacity or locality.

**cycle rank**  
The dimension of the cycle space \( \dim_{\mathbb{F}_2} Z_1(G) \). A canonical global invariant separating URF from non-local regimes.

**homogeneity**  
Uniformity of local configuration types across an instance. Persistent homogeneity under refinement leads to rigidity.

**heterogeneity**  
Diversity of local configuration types. Necessary for progress under bounded refinement.

**witness**  
A bounded object (configuration, parity, dependency) certifying distinguishability or progress. Witness size is capacity-controlled.

**oracle**  
An external information source. Oracles with unbounded output or precision violate capacity; global oracles violate locality.

**capacity class**  
A family of processes sharing the same per-step capacity bound \(C_{\max}\). Sharp bounds are stated per capacity class.

**refinement wall**  
A theorem asserting impossibility of further progress within a given capacity and locality regime.

**terminal wall**  
A wall that cannot be bypassed without violating admissibility. Marks a regime boundary, not a limitation of technique.

**regime exit**  
Any explicit step that leaves the admissible refinement regime (capacity violation, locality violation, or oracle use).

**global-invariant regime**  
A regime in which computation relies on non-local quantities. Outside URF by definition.

**finite exhaustion**  
Analysis method where infinite objects are studied only through increasing finite instances with controlled parameters.

**limit rigidity**  
Divergence of entropy depth along an exhaustion, implying non-termination of the directed limit.

**normalization choice**  
A scale or unit fixed for convenience in the absence of a natural bound. Has no invariant meaning without capacity limits.

