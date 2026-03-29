namespace CacheTool

def main (args : List String) : IO UInt32 := do
  match args with
  | "get" :: _ =>
      IO.println "cache get (deterministic stub)"
      pure 0
  | _ =>
      IO.println "usage: cache get"
      pure 0

end CacheTool

def main := CacheTool.main
