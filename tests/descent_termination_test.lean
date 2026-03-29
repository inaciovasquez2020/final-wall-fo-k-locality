import URF.URFInvariant

namespace Test

open URF

def sampleConfig : Configuration Nat :=
  { data := 0, rank := 3 }

#eval sampleConfig.rank

end Test
