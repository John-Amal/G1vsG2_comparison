import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_2t_all_exp.png')

# The Y axis has labels 11 to 18.
# We need to map pixels to °C.
# Find the pixels for the y-axis grid lines. There are faint gray horizontal lines.
# Look at x=300 (before the curves start, in the yellow area).
grid_lines = []
for y in range(img.shape[0]):
    r, g, b = img[y, 300][:3]
    if r > 0.8 and g > 0.8 and b > 0.8 and r < 0.95: # grid lines are light gray
        grid_lines.append(y)

# Let's find horizontal dashed colored lines 
def find_dashed_mean(cond):
    y_counts = {}
    for x in range(400, 3000, 2):
        for y in range(img.shape[0]):
            if cond(img[y,x,0], img[y,x,1], img[y,x,2]):
                y_counts[y] = y_counts.get(y, 0) + 1
    # Find peaks in y_counts
    peaks = sorted([(c,y) for y,c in y_counts.items() if c > 100], reverse=True)
    return peaks[:5]

b_means = find_dashed_mean(lambda r,g,b: b>0.7 and r<0.5)
g_means = find_dashed_mean(lambda r,g,b: g>0.4 and r<0.5 and b<0.5)
o_means = find_dashed_mean(lambda r,g,b: r>0.7 and g>0.3 and b<0.6)

print("Grid lines:", grid_lines[:10], "...")
print("Blue mean Ys (c,y):", b_means)
print("Green mean Ys (c,y):", g_means)
print("Orange mean Ys (c,y):", o_means)
