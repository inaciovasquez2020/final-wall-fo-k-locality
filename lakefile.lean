import Lake
open Lake DSL

package URFCore

@[default_target]
lean_lib URFCore where
 srcDir := "URFCore"

@[default_target]
lean_exe urf_core where
 root := `Provenance
