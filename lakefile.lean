import Lake
open Lake DSL

package urf_core where
  leanOptions := #[⟨`pp.unicode.fun, true⟩]

lean_lib URFCore where
  -- add src dirs later if needed


require lake_cache_tool from "." / "tools" / "lake-cache-tool"
