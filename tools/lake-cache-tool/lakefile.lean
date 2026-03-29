import Lake
open Lake DSL

package lake_cache_tool

lean_lib CacheTool

@[default_target]
lean_exe cache where
  root := `CacheTool.Main
