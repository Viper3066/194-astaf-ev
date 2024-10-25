
kB= 1.380649e-23
mu_e = -9.28476377e-24
N_A = 6.02214076e+23
c = 2.99792458e8
G = 6.67430e-11
mu_e_unc = 2.3e-31
G_unc = 1.5e-15
format_spec = "{:.4e}"
print(f"kB = {format_spec.format(kB)} J/K")
print(f"mu_e = {format_spec.format(mu_e)} J/T")
print(f"N_A = {format_spec.format(N_A)} mol^-1")
print(f"c = {format_spec.format(c)} m/s")
format_spec_capital_E = "{:+.2E}"
G_units = 'Nm^2/kg^2'
mu_e_units = 'J/T'
print(f"G = {format_spec_capital_E.format(G)} [{G_units}]")
print(f"mu_e = {format_spec_capital_E.format(mu_e)} [{mu_e_units}]")
def format_with_uncertainty(a,b):
    b1= f"{b:.1e}"
    b2 = b1.split('e')[0].replace('.', '')
    a1 = f"{a:.5e}"
    return f"{a1[:-5]}({b2}){a1[-5:]}"
print(f"G = {format_with_uncertainty(G, G_unc)} {G_units}")
print(f"mu_e = {format_with_uncertainty(mu_e, mu_e_unc)} {mu_e_units}")
