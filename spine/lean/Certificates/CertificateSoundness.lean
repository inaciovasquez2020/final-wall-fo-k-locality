namespace URF

universe u

structure Certificate where
  payload : Type u

def Verifier (C : Certificate) : Type u := C.payload → Bool
def Property (C : Certificate) : Type u := C.payload → Prop

structure SoundnessContract (C : Certificate) (V : Verifier C) (P : Property C) : Prop where
  sound : ∀ c, V c = true → P c

structure CompletenessContract (C : Certificate) (V : Verifier C) (P : Property C) : Prop where
  complete : ∀ c, P c → V c = true

end URF
