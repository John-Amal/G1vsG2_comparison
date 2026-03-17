import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_hist_2017-2024_2t_comparison.png')

# Black (ERA5): r<0.2, g<0.2, b<0.2
# Blue (G1): b>0.7, r<0.2, g<0.2
# Red (G2): r>0.7, g<0.2, b<0.2

def find_peaks(cond, name):
    for x in range(600, 700):  # Summer 2018 range
        ys = []
        for y in range(img.shape[0]):
            r,g,b = img[y,x][:3]
            if cond(r,g,b): ys.append(y)
        if len(ys) > 0:
            print(f"{name} at x={x}: min Y (peak temp) = {min(ys)}")
            break

find_peaks(lambda r,g,b: sum([r,g,b])<0.6, "ERA5 (Black)")
find_peaks(lambda r,g,b: b>0.7 and r<0.3 and g<0.3, "Gen1 (Blue)")
find_peaks(lambda r,g,b: r>0.7 and g<0.3 and b<0.3, "Gen2 (Red)")

