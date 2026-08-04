##################################################
# This script calculated masses and sizes of TNOs
# according to fits and saves the result.
##################################################


import numpy as np
import pandas as pd


# input data
df = pd.read_csv("../output/tnos_debiased_classified.csv", sep=",", header=0, comment="#")
save_file = "../output/tnos_debiased_classified_masses.csv"


def broken_exp10(B, x):
    """
    Continuous broken exponential in base 10:
        y = A * 10^(B1 * x)               for x < xb
        y = A * 10^(B1 * xb) * 10^(B2 * (x - xb))   for x >= xb
    """
    alpha, beta1, beta2 = B
    xb = 7.22
    x = np.asarray(x)
    y = np.where(x < xb,
                 alpha * 10 ** (beta1 * x),
                 alpha * 10 ** (beta1 * xb) * 10 ** (beta2 * (x - xb)))
    return y


def broken_pl(B, x):
    # B = [A, alpha2]
    A, alpha = B
    s_break = 210
    x = np.asarray(x)
    # For x < s_break, exponent = 0 => value = A
    y = np.where(
        x < s_break,
        A,
        A * (x / s_break) ** (alpha)
    )
    return y


def density_error(B, x):
    alpha, dalpha, beta, dbeta = B
    x_break = 210
    x = np.asarray(x)
    # For x < s_break, exponent = 0 => value = A
    dy2 = np.where(
        x < x_break,
        dalpha ** 2,
        ((x / x_break) ** beta * dalpha) ** 2 + (np.log(x / x_break) * alpha * (x / x_break) ** beta * dbeta) ** 2
    )
    return np.sqrt(dy2)


def size_error(B, x):
    alpha, dalpha, beta1, dbeta1, beta2, dbeta2 = B
    x = np.asarray(x)

    xb = 7.22

    ds2 = np.where(x < xb,
                   (10 ** (beta1 * x) * dalpha) ** 2 + (np.log(10) * alpha * x * 10 ** (beta1 * x) * dbeta1) ** 2,
                   (10 ** (beta1 * xb) * 10 ** (beta2 * (x - xb)) * dalpha) ** 2
                   + (np.log(10) * alpha * xb * 10 ** (beta1 * xb) * dbeta1 * 10 ** (beta2 * (x - xb))) ** 2
                   + (alpha * 10 ** (beta1 * xb) * np.log(10) * (x - xb) * 10 ** (beta2 * (x - xb)) * dbeta2) ** 2)

    return np.sqrt(ds2)


# results from fits
def diameter_fit(H):
    # fit errors
    alpha_fit = 1680
    d_alpha_fit = 30

    beta1_fit = -0.125
    d_beta1_fit = 0.002

    beta2_fit = -0.205
    d_beta2_fit = 0.006

    s = broken_exp10([alpha_fit, beta1_fit, beta2_fit], H)
    ds = size_error([alpha_fit, d_alpha_fit, beta1_fit, d_beta1_fit, beta2_fit, d_beta2_fit], H)


    return s, ds


def density_fit(s):
    # fit errors
    alpha_fit = 518
    d_alpha_fit = 25

    beta_fit = 0.53
    d_beta_fit = 0.02

    rho = broken_pl([alpha_fit, beta_fit], s)
    drho = density_error([alpha_fit, d_alpha_fit, beta_fit, d_beta_fit], s)


    return rho, drho


def mass(s, rho):
    mass = np.pi / 6 * s ** 3 * rho
    return mass


def mass_error(s, ds, rho, drho):
    dm2 = ((np.pi / 2) * s ** 2 * rho * ds) ** 2 + ((np.pi / 6) * s ** 3 * drho) ** 2

    return np.sqrt(dm2)


def calc_mass(H):
    s, ds = diameter_fit(H)
    rho, drho = density_fit(s)

    m = mass(s * 1e3, rho)
    dm = mass_error(s * 1e3, ds * 1e3, rho, drho)


    return m, dm



df = df.dropna(subset=['H'], ignore_index=True)
df = df[df["H"] < 50]
df = df[df["prob"] > 0]
df["N_deb"] = 1 / df["prob"]
abs_mag = df["H"].to_numpy()

masses = []
masses_err = []

sizes = []
sizes_err = []

for i in range(len(df)):
    size_kbo, size_kbo_err = diameter_fit(abs_mag[i])
    mass_kbo, mass_kbo_err = calc_mass(abs_mag[i])
    masses.append(mass_kbo)
    masses_err.append(mass_kbo_err)
    sizes.append(size_kbo)
    sizes_err.append(size_kbo_err)

m_earth = 5.97217e24

df["D"] = sizes
df["dD"] = sizes_err
df["m"] = np.array(masses) / (1e-3 * m_earth)
df["dm"] = np.array(masses_err) / (1e-3 * m_earth)

df.to_csv(save_file, sep=",", index=False)

with open(save_file, "w") as f:
    # Metadata header
    f.write("# Debiased Kuiper Belt Objects\n")
    f.write("# Columns:\n")
    f.write("#   type:          dynamical type\n")
    f.write("#   Designation:   object designation\n")
    f.write("#   a:             semimajor axis [au]\n")
    f.write("#   e:             eccentricity\n")
    f.write("#   inc:           inclination [deg]\n")
    f.write("#   peri:          argument of perihelion [deg]\n")
    f.write("#   node:          longitude of ascending node [deg]\n")
    f.write("#   H:             absolute magnitude\n")
    f.write("#   prob:          survey detection probability\n")
    f.write("#   res:           mean motion resonance\n")
    f.write("#   Ndeb:          debiasing factor\n")
    f.write("#   D:             diameter [km]\n")
    f.write("#   dD:            diameter error [km]\n")
    f.write("#   m:             mass [0.001 M_earth]\n")
    f.write("#   dm:            mass error [0.001 M_earth]\n")
    f.write("#\n")

    # Append CSV data
    df.to_csv(f, index=False)



