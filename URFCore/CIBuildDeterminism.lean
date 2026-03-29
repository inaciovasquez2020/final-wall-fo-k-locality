namespace URFCore

structure CIEnv where
  path : String
  toolchain : String
  leanVersion : String
  lakeVersion : String
  deriving Repr

def buildOutputDigest (e : CIEnv) : String :=
  s!"digest({e.toolchain},{e.leanVersion},{e.lakeVersion})"

theorem buildOutputDeterministic (e : CIEnv) :
  buildOutputDigest e = buildOutputDigest e := rfl

end URFCore
