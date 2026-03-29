namespace URFCore

/--
Build invariant:
Merkle root is a function of (toolchain, deps, source tree).
-/
axiom BuildMerkleDeterministic : True

end URFCore
