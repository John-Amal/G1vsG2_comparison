import matplotlib.pyplot as plt

img = plt.imread('/Users/amjohn001/work/antigravity/git_cd_ci/G1vsG2_comparison/plots/TS_2t_all_exp.png')

# blue condition
cond = lambda r,g,b: b>0.7 and r<0.5

# Look at y=243 and y=269 across a range of x to see which one is continuous
y1, y2 = 243, 269
row1_pixels = sum([1 for x in range(700, 750) if cond(*img[y1,x][:3])])
row2_pixels = sum([1 for x in range(700, 750) if cond(*img[y2,x][:3])])

print("Y=243 (warmer line) has", row1_pixels, "blue pixels in 50 wide strip")
print("Y=269 (cooler line) has", row2_pixels, "blue pixels in 50 wide strip")
