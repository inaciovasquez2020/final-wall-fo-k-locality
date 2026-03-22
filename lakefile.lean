import Lake
open Lake DSL

package URFCore where
 version := "0.1.0"

lean_lib URFCore

@[default_target]
lean_exe urf_core where
 root := `URFCore
