##################################################
# This script assigns every KBO to one of the 
# commonly used dynamical classes (classical, resonant, 
# scattering detached) using the conditions adopted 
# from Gladman & Volk 2021. For the resonant 
# population, the results of the orbit integrations
# from the Dark Energy Survey (Elliot et al. 2005)
# were used (see https://www2.boulder.swri.edu/~buie/kbo/desclass.html).
# Note, that if you want to also use the debiasing
# routing, you can only apply the classification
# afterwards, as the debiasing will not work otherwise.
##################################################



import pandas as pd
import numpy as np

# Results of the debiasing
file_path_kbos = '../output/tnos_debiased.csv'
save_file = "../output/tnos_debiased_classified.csv"


file_path_tnos = '../input/TNOs.txt'

# Read the text file, skipping the first line and using fixed-width format
column_names = [
    "Designation", "Prov", "Des", "q", "Q", "H", "Epoch", "M", "Peri",
    "Node", "Incl", "e", "a", "Opps", "Ref", "Designation_name", "Discovery_date_site_discoverer"
]

# Define the fixed widths for each column based on the structure of the file
column_widths = [
    27, 5, 7, 7, 10, 7, 10, 7, 6, 6, 6, 6, 9, 9, 19, 33, 48
]

# Read the file using pandas.read_fwf
df = pd.read_fwf(file_path_tnos, widths=column_widths, names=column_names, skiprows=1)

df['Designation'] = df['Designation'].replace(r"[()]", "", regex=True)

# import debiasesed data
df_deb = pd.read_csv(file_path_kbos, header=0, sep=',', comment="#")

df_deb["des_num"] = df['Designation']


# import list of resonant objects
df_1_1 = pd.read_csv("../data/resonants/1_1.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_1_1[0])
df_deb.loc[mask_res, "res"] = "1_1"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_1_1[0])
df_deb.loc[mask_res, "res"] = "1_1"
df_deb.loc[mask_res, "type"] = "res"

df_2_1 = pd.read_csv("../data/resonants/2_1.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_2_1[0])
df_deb.loc[mask_res, "res"] = "2_1"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_2_1[0])
df_deb.loc[mask_res, "res"] = "2_1"
df_deb.loc[mask_res, "type"] = "res"

df_3_1 = pd.read_csv("../data/resonants/3_1.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_3_1[0])
df_deb.loc[mask_res, "res"] = "3_1"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_3_1[0])
df_deb.loc[mask_res, "res"] = "3_1"
df_deb.loc[mask_res, "type"] = "res"

df_3_2 = pd.read_csv("../data/resonants/3_2.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_3_2[0])
df_deb.loc[mask_res, "res"] = "3_2"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_3_2[0])
df_deb.loc[mask_res, "res"] = "3_2"
df_deb.loc[mask_res, "type"] = "res"

df_4_1 = pd.read_csv("../data/resonants/4_1.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_4_1[0])
df_deb.loc[mask_res, "res"] = "4_1"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_4_1[0])
df_deb.loc[mask_res, "res"] = "4_1"
df_deb.loc[mask_res, "type"] = "res"

df_4_3 = pd.read_csv("../data/resonants/4_3.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_4_3[0])
df_deb.loc[mask_res, "res"] = "4_3"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_4_3[0])
df_deb.loc[mask_res, "res"] = "4_3"
df_deb.loc[mask_res, "type"] = "res"

df_5_1 = pd.read_csv("../data/resonants/5_1.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_5_1[0])
df_deb.loc[mask_res, "res"] = "5_1"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_5_1[0])
df_deb.loc[mask_res, "res"] = "5_1"
df_deb.loc[mask_res, "type"] = "res"

df_5_2 = pd.read_csv("../data/resonants/5_2.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_5_2[0])
df_deb.loc[mask_res, "res"] = "5_2"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_5_2[0])
df_deb.loc[mask_res, "res"] = "5_2"
df_deb.loc[mask_res, "type"] = "res"

df_5_3 = pd.read_csv("../data/resonants/5_3.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_5_3[0])
df_deb.loc[mask_res, "res"] = "5_3"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_5_3[0])
df_deb.loc[mask_res, "res"] = "5_3"
df_deb.loc[mask_res, "type"] = "res"

df_5_4 = pd.read_csv("../data/resonants/5_4.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_5_4[0])
df_deb.loc[mask_res, "res"] = "5_4"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_5_4[0])
df_deb.loc[mask_res, "res"] = "5_4"
df_deb.loc[mask_res, "type"] = "res"

df_6_1 = pd.read_csv("../data/resonants/6_1.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_6_1[0])
df_deb.loc[mask_res, "res"] = "6_1"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_6_1[0])
df_deb.loc[mask_res, "res"] = "6_1"
df_deb.loc[mask_res, "type"] = "res"

df_7_2 = pd.read_csv("../data/resonants/7_2.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_7_2[0])
df_deb.loc[mask_res, "res"] = "7_2"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_7_2[0])
df_deb.loc[mask_res, "res"] = "7_2"
df_deb.loc[mask_res, "type"] = "res"

df_7_3 = pd.read_csv("../data/resonants/7_3.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_7_3[0])
df_deb.loc[mask_res, "res"] = "7_3"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_7_3[0])
df_deb.loc[mask_res, "res"] = "7_3"
df_deb.loc[mask_res, "type"] = "res"

df_7_4 = pd.read_csv("../data/resonants/7_4.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_7_4[0])
df_deb.loc[mask_res, "res"] = "7_4"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_7_4[0])
df_deb.loc[mask_res, "res"] = "7_4"
df_deb.loc[mask_res, "type"] = "res"

df_7_5 = pd.read_csv("../data/resonants/7_5.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_7_5[0])
df_deb.loc[mask_res, "res"] = "7_5"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_7_5[0])
df_deb.loc[mask_res, "res"] = "7_5"
df_deb.loc[mask_res, "type"] = "res"

df_8_3 = pd.read_csv("../data/resonants/8_3.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_8_3[0])
df_deb.loc[mask_res, "res"] = "8_3"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_8_3[0])
df_deb.loc[mask_res, "res"] = "8_3"
df_deb.loc[mask_res, "type"] = "res"

df_8_5 = pd.read_csv("../data/resonants/8_5.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_8_5[0])
df_deb.loc[mask_res, "res"] = "8_5"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_8_5[0])
df_deb.loc[mask_res, "res"] = "8_5"
df_deb.loc[mask_res, "type"] = "res"

df_9_1 = pd.read_csv("../data/resonants/9_1.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_9_1[0])
df_deb.loc[mask_res, "res"] = "9_1"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_9_1[0])
df_deb.loc[mask_res, "res"] = "9_1"
df_deb.loc[mask_res, "type"] = "res"

df_9_2 = pd.read_csv("../data/resonants/9_2.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_9_2[0])
df_deb.loc[mask_res, "res"] = "9_2"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_9_2[0])
df_deb.loc[mask_res, "res"] = "9_2"
df_deb.loc[mask_res, "type"] = "res"

df_9_4 = pd.read_csv("../data/resonants/9_4.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_9_4[0])
df_deb.loc[mask_res, "res"] = "9_4"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_9_4[0])
df_deb.loc[mask_res, "res"] = "9_4"
df_deb.loc[mask_res, "type"] = "res"

df_9_5 = pd.read_csv("../data/resonants/9_5.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_9_5[0])
df_deb.loc[mask_res, "res"] = "9_5"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_9_5[0])
df_deb.loc[mask_res, "res"] = "9_5"
df_deb.loc[mask_res, "type"] = "res"

df_10_3 = pd.read_csv("../data/resonants/10_3.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_10_3[0])
df_deb.loc[mask_res, "res"] = "10_3"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_10_3[0])
df_deb.loc[mask_res, "res"] = "10_3"
df_deb.loc[mask_res, "type"] = "res"

df_10_7 = pd.read_csv("../data/resonants/10_7.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_10_7[0])
df_deb.loc[mask_res, "res"] = "10_7"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_10_7[0])
df_deb.loc[mask_res, "res"] = "10_7"
df_deb.loc[mask_res, "type"] = "res"

df_11_2 = pd.read_csv("../data/resonants/11_2.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_11_2[0])
df_deb.loc[mask_res, "res"] = "11_2"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_11_2[0])
df_deb.loc[mask_res, "res"] = "11_2"
df_deb.loc[mask_res, "type"] = "res"

df_11_3 = pd.read_csv("../data/resonants/11_3.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_11_3[0])
df_deb.loc[mask_res, "res"] = "11_3"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_11_3[0])
df_deb.loc[mask_res, "res"] = "11_3"
df_deb.loc[mask_res, "type"] = "res"

df_11_5 = pd.read_csv("../data/resonants/11_5.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_11_5[0])
df_deb.loc[mask_res, "res"] = "11_5"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_11_5[0])
df_deb.loc[mask_res, "res"] = "11_5"
df_deb.loc[mask_res, "type"] = "res"

df_11_6 = pd.read_csv("../data/resonants/11_6.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_11_6[0])
df_deb.loc[mask_res, "res"] = "11_6"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_11_6[0])
df_deb.loc[mask_res, "res"] = "11_6"
df_deb.loc[mask_res, "type"] = "res"

df_11_7 = pd.read_csv("../data/resonants/11_7.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_11_7[0])
df_deb.loc[mask_res, "res"] = "11_7"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_11_7[0])
df_deb.loc[mask_res, "res"] = "11_7"
df_deb.loc[mask_res, "type"] = "res"

df_12_5 = pd.read_csv("../data/resonants/12_5.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_12_5[0])
df_deb.loc[mask_res, "res"] = "12_5"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_12_5[0])
df_deb.loc[mask_res, "res"] = "12_5"
df_deb.loc[mask_res, "type"] = "res"

df_12_7 = pd.read_csv("../data/resonants/12_7.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_12_7[0])
df_deb.loc[mask_res, "res"] = "12_7"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_12_7[0])
df_deb.loc[mask_res, "res"] = "12_7"
df_deb.loc[mask_res, "type"] = "res"

df_13_4 = pd.read_csv("../data/resonants/13_4.txt", header=None, sep='\t')
mask_res = df_deb["Designation"].isin(df_13_4[0])
df_deb.loc[mask_res, "res"] = "13_4"
df_deb.loc[mask_res, "type"] = "res"
mask_res = df_deb["des_num"].isin(df_13_4[0])
df_deb.loc[mask_res, "res"] = "13_4"
df_deb.loc[mask_res, "type"] = "res"

# scattering
mask_scat = df_deb["type"].isna() & ((df_deb["a"] * (1 - df_deb["e"])) <= 38)
df_deb.loc[mask_scat, "type"] = "scat"

# detached
mask_det = df_deb["type"].isna() & ((df_deb["a"] * (1 - df_deb["e"])) > 38) & (df_deb["a"] > 47.4) & (
        df_deb["e"] > 0.24)
df_deb.loc[mask_det, "type"] = "det"

# classical
mask_clas = df_deb["type"].isna()
df_deb.loc[mask_clas, "type"] = "clas"

# move type to beginning of table
column_to_move = df_deb.pop("type")
df_deb.insert(0, "type", column_to_move)
df_deb = df_deb.drop("des_num", axis=1)


# add metadata header
df_deb.to_csv(save_file, index=False, sep=",")

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
    f.write("#\n")

    # Append CSV data
    df_deb.to_csv(f, index=False)
