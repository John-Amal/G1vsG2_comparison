import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_2t_all_exp.png')

# Find horizontal dashed lines.
# They span from roughly x=400 to x=3000
# Let's sum the pixels in each row for the colors to see the big spikes in horizontal lines
import collections

def find_horizontals(cond):
    y_counts = collections.defaultdict(int)
    for x in range(400, 3000, 5):
        for y in range(img.shape[0]):
            r,g,b = img[y,x][:3]
            if cond(r,g,b):
                y_counts[y] += 1
    # print top Ys
    for y, count in sorted(y_counts.items(), key=lambda kv: kv[1], reverse=True)[:5]:
        if count > 100:
            print("Y=", y, "count=", count)

print("Cont (Blue) dashed means:")
find_horizontals(lambda r,g,b: b>0.7 and r<0.5)

print("Hist (Green) dashed means:")
find_horizontals(lambda r,g,b: g>0.4 and r<0.5 and b<0.5)

print("2k (Orange) dashed means:")
find_horizontals(lambda r,g,b: r>0.7 and g>0.2 and b<0.6)

