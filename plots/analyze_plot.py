import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_2t_all_exp.png')
print("Image shape:", img.shape)
# img is usually float32 [0, 1] for pngs 

# Find light blue pixels (cont)
# Let's say blue channel > 0.8, red < 0.5
def get_blue_pixels(x_col):
    col = img[:, x_col]
    blue_ys = []
    for y in range(len(col)):
        r, g, b = col[y][:3]
        if b > 0.7 and r < 0.5:
            blue_ys.append((y, b, r, g))
    return blue_ys

b2017 = get_blue_pixels(320)
print(f"Blue pixels at x=320 (2017): {len(b2017)}")
if b2017: print("  mean Y:", np.mean([y[0] for y in b2017]))

b2018 = get_blue_pixels(650)
print(f"Blue pixels at x=650 (2018 summer approx): {len(b2018)}")
if b2018:
    ys = [y[0] for y in b2018]
    print("  mean Y:", np.mean(ys), "min Y:", np.min(ys), "max Y:", np.max(ys))

