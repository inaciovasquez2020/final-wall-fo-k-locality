import Lake
open Lake DSL

package lake_cache_tool

@[default_target]
lean_exe cache where
  root := `CacheMain
