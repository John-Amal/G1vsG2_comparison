import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_2t_all_exp.png')

# Legend:
# cont Gen1 = blue dotted
# cont Gen2 = blue solid
# hist Gen1 = green dotted
# hist Gen2 = green solid
# 2k Gen1 = orange dotted
# 2k Gen2 = orange solid

# Let's find horizontal dashed lines
import collections

def find_dashed(cond):
    y_counts = collections.defaultdict(int)
    for x in range(500, 3000, 5):
        for y in range(img.shape[0]):
            r,g,b = img[y,x][:3]
            if cond(r,g,b):
                y_counts[y] += 1
    # print top Ys
    res = []
    for y, count in sorted(y_counts.items(), key=lambda kv: kv[1], reverse=True)[:5]:
        if count > 100:
            res.append(y)
    return sorted(res)

print("Cont (Blue) dashed Ys (lower Y = higher temp):", find_dashed(lambda r,g,b: b>0.7 and r<0.5))
print("Hist (Green) dashed Ys (lower Y = higher temp):", find_dashed(lambda r,g,b: g>0.4 and r<0.5 and b<0.5))
print("2k (Orange) dashed Ys (lower Y = higher temp):", find_dashed(lambda r,g,b: r>0.7 and g>0.2 and b<0.6))

