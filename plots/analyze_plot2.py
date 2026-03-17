import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_2t_all_exp.png')

# Define rough colors
# Blue (Cont): r<0.5, b>0.7
# Green (Hist): g>0.5, b<0.5, r<0.5
# Orange (2k): r>0.7, g>0.2, b<0.5

def get_ys(x, color_cond):
    col = img[:, x]
    ys = []
    for y in range(len(col)):
        r, g, b = col[y][:3]
        if color_cond(r, g, b):
            ys.append(y)
    return ys

def print_stats(color_name, cond):
    # Sample in 2018 at around x=700
    ys = get_ys(700, cond)
    if not ys:
        print(f"{color_name}: no pixels found")
        return
    
    # cluster them to separate the two lines
    from sklearn.cluster import KMeans
    ys_arr = np.array(ys).reshape(-1, 1)
    if len(ys) > 5:
        kmeans = KMeans(n_clusters=2, random_state=0).fit(ys_arr)
        centers = kmeans.cluster_centers_.flatten()
        print(f"{color_name} centers (lower y = higher temp): {sorted(centers)}")
    else:
        print(f"{color_name} ys: {ys}")

print_stats("Blue", lambda r,g,b: b>0.7 and r<0.5)
print_stats("Green", lambda r,g,b: g>0.4 and r<0.5 and b<0.5)
print_stats("Orange", lambda r,g,b: r>0.7 and g>0.3 and b<0.6)
