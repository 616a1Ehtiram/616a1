# Siqnal gücünü dBm-dən millivata çeviririk: P(mW)=10^(dBm/10) 
rsrp_dbm = -95
p_mw = 10 ** (rsrp_dbm/10)
print (f"{rsrp_dbm} dBm = {p_mw: .2e} mw") 
# Bir neçə ölçmə: hansılar zəif siqnaldır (< -105 dBm)?
values =[-85, -97, -110, -102, -118]
for v in values:
    if v < -105:
        print (v, "dBm - zəif siqnal")
    else:
        print (v, "dBm - normal")