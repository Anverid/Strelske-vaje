import math
g = 10
v = float(input("Vnesi hitrost v m/s: "))
kot_stopinje = float(input("Vnesi kot v stopinjah: "))
kot_radians = kot_stopinje * (math.pi / 180)
v_pow2 = v * v
sin_kota = math.sin(2 * kot_radians)
razdalja = (v_pow2 * sin_kota) / g
print("Če iz topa ustrelimo kroglo s hitrostjo " + str(v) + "m/s in pod kotom " +
      str(kot_stopinje) + "° je radalja izstreljene krogle " + str(razdalja) + "m.")
