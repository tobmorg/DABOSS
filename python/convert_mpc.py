##################################################
# This script reads the ascii files for TNOs and 
# Centaurs from the MPC Database, concatenates them
# and saves the data needed for debiasing in a 
# comma-separated file.
#
# INPUT:
# ------
# ../data/TNOs.txt (https://www.minorplanetcenter.net/iau/lists/TNOs.html)
# ../data/Centaurs.txt (https://www.minorplanetcenter.net/iau/lists/Centaurs.html)
#
# -> These files must me placed in the data directory
# in the exact same form as they cane be downloaded
# from the MPC database.
##################################################


import pandas as pd

# Path to the text file
tnos = '../input/TNOs.txt'
centaurs = '../input/Centaurs.txt'

# Path to the output CSV file
save_file = '../data/tnos_mpc.csv'

# Read the text file, skipping the first line and using fixed-width format
column_names = [
    "Designation", "Prov", "Des", "q", "Q", "H", "Epoch", "M", "Peri", 
    "Node", "Incl", "e", "a", "Opps", "Ref", "Designation_name", "Discovery_date_site_discoverer"
]

# Define the fixed widths for each column based on the structure of the file
column_widths = [
    27, 5, 7, 7, 10, 7, 10, 7, 6, 6, 6, 6, 9, 9, 19, 33, 48
]

# Read the file using
df_tnos = pd.read_fwf(tnos, widths=column_widths, names=column_names, skiprows=1)
df_centaurs = pd.read_fwf(centaurs, widths=column_widths, names=column_names, skiprows=1)

df = pd.concat([df_tnos, df_centaurs], axis=0)

dfFormatted = pd.DataFrame([])

dfFormatted["#Designation"] = df["Designation_name"]    # Designation name ('#' added for comment in c++ debiasing routine)
dfFormatted["a"] = df["a"]                              # semi major axis [au]
dfFormatted["e"] = df["e"]                              # eccentricity
dfFormatted["inc"] = df["Incl"]                         # inclination [deg]    
dfFormatted["peri"] = df["Peri"]                        # argument of pericentre [deg]
dfFormatted["Omega"] = df["Node"]                       # longitude of the ascending node [deg]
dfFormatted["H"] = df["H"]                              # absolute magnitude (Solar System definition)

# print(df["Designation"], df["Designation_name"])


df1 = dfFormatted

# remove rows with incomplete data
dfFormatted = dfFormatted.dropna(subset=["a"])
dfFormatted = dfFormatted.dropna(subset=["e"])
dfFormatted = dfFormatted.dropna(subset=["inc"])
dfFormatted = dfFormatted.dropna(subset=["peri"])
dfFormatted = dfFormatted.dropna(subset=["Omega"])
dfFormatted = dfFormatted.dropna(subset=["H"])


df2 = dfFormatted

# Rows in df2 that are NOT in df1
missing = df2.merge(df1.drop_duplicates(),
                    how='right',
                    indicator=True)

missing = missing[missing['_merge'] == 'left_only']

# print(len(df1))
# print(len(df2))

# print(missing)


# only_in_df1 = df1[~df1['#Designation'].isin(df2['#Designation'])]
# only_in_df2 = df2[~df2['#Designation'].isin(df1['#Designation'])]

# print("Only in df1:")
# print(only_in_df1)

# print("Only in df2:")
# print(only_in_df2)


dfFormatted.to_csv(save_file, sep=",", index=False)


