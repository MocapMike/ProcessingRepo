import pandas as pd

def reconfigure_forceplate(file_path, start_col, end_col):
    # Reading the file assuming it's tab-delimited. You may have to adjust the delimiter.
    df = pd.read_csv(file_path, delimiter='\s+', engine='python', skiprows=7)

    # Selecting the specified columns
    df = df.iloc[:, start_col:end_col]
    
    # Renaming the columns
    df.columns = new_columns[:end_col - start_col]


    return df

# Columns to rename


new_columns = ["ground_force_vx", "ground_force_vy", "ground_force_vz", "ground_force_px", "ground_force_py", "ground_force_pz",
               "l_ground_force_vx", "l_ground_force_vy", "l_ground_force_vz", "l_ground_force_px", "l_ground_force_py", "l_ground_force_pz",
               "ground_torque_x", "ground_torque_y", "ground_torque_z", "l_ground_torque_x", "l_ground_torque_y", "l_ground_torque_z"]


start_col = 1
end_col = 9


walk_0004_L1_tracked = reconfigure_forceplate('/Users/mdn/Documents/DATA/V3D_Opensim_Comparison/TAG_800_A1/QTM2V3D/trc_mot/walk_0004_L1_tracked_trimmed.mot', start_col, end_col)

print(walk_0004_L1_tracked.head())

f = 23