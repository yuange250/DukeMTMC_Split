from scipy.io import loadmat
import pandas as pd

m = loadmat("F:\Dataset\DukeMTMC\match_data.mat")
df_columns = ["person_id", "camera_id", "frame_id_in_origin_video", "frame_img_name", "x", "y", "w", "h"]
result_path = "F:\Dataset\DukeMTMC\match_data.csv"
result_file = open(result_path, 'w')
result_file.write(",".join(df_columns) + "\n")
data = m['match_data']
for i in range(m['match_data'].shape[0]):
    if i % 100000 == 0:
        print("process:%d/%d"%(i, m['match_data'].shape[0]))
    if len(data[i][0][0]) != 0:
        values = []
        values.append(str(data[i][1][0][0]))
        values.append(str(data[i][0][0][0]))
        values.append(str(data[i][2][0][0]))
        values.append(data[i][11][0])
        values.append(str(data[i][3][0][0]))
        values.append(str(data[i][4][0][0]))
        values.append(str(data[i][5][0][0]))
        values.append(str(data[i][6][0][0]))
        result_file.write(",".join(values) + "\n")

result_file.close()