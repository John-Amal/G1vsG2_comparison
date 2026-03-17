import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_2t_all_exp.png')

def get_y_profile(color_cond):
    # Sum the matching pixels across rows for a single column x=700
    ys = []
    for y in range(img.shape[0]):
        r, g, b = img[y, 700][:3]
        if color_cond(r, g, b):
            ys.append(y)
    return ys

b_ys = get_y_profile(lambda r,g,b: b>0.7 and r<0.5)
g_ys = get_y_profile(lambda r,g,b: g>0.4 and r<0.5 and b<0.5)
o_ys = get_y_profile(lambda r,g,b: r>0.7 and g>0.2 and b<0.6)

print("Blue Ys:", b_ys)
print("Green Ys:", g_ys)
print("Orange Ys:", o_ys)

b_ys_2017 = []
for y in range(img.shape[0]):
    r,g,b = img[y, 300][:3]
    if b>0.7 and r<0.5: b_ys_2017.append(y)
print("Blue Ys 2017:", b_ys_2017)

g_ys_2017 = []
for y in range(img.shape[0]):
    r,g,b = img[y, 300][:3]
    if g>0.4 and r<0.5 and b<0.5: g_ys_2017.append(y)
print("Green Ys 2017:", g_ys_2017)

o_ys_2017 = []
for y in range(img.shape[0]):
    r,g,b = img[y, 300][:3]
    if r>0.7 and g>0.2 and b<0.6: o_ys_2017.append(y)
print("Orange Ys 2017:", o_ys_2017)


