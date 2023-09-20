import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("insurance.csv",nrows=50)
# print(data)
male=data[data['sex']=='male']
female=data[data['sex']=='female']
print(data['sex'].unique())
date=(data['BMI'].unique())
(date.sort())
print(date)
# histogram
male['age'].plot(kind='hist',label="AGE",color='r',fontsize=10,density='true')
plt.title('scatter plot -histogram')
plt.xlabel('SepalWidthCm')
plt.show()
male.mean

# scatter plot

male.plot(x="age", y="BMI", kind="scatter", label='MALE',color='r')
plt.title('Scatter Plot - MALE')
plt.xlabel('AGE')
plt.ylabel('BDI')
plt.show()

# Line Plot
male["BMI"].plot(kind="line",label='male', color='black',linewidth='1.5', ls=':')
plt.axis([0,50,17,41])
plt.title('Line Plot')
plt.xlabel('BMI')
plt.show()

# areaplot
male.plot.area(stacked=True)
plt.show()


# bargraph
type=list(data['sex'].unique())
count=list(data['sex'].value_counts())
Avg=list(data.groupby('sex')["age"].mean())
print(Avg)
plt.bar(type,Avg,color=['maroon','yellow','blue'],width=0.4)
# .barh------height=0.4
plt.title('Bar Plot')
plt.xlabel('BMI')
plt.ylabel('AverageBMI')
plt.show()


# pie chart
e=(0,0)
Avg=list(data.groupby('sex')["BMI"].mean())
plt.pie(Avg, explode=e,labels=['male','female'])
plt.title("Pie chart")
plt.legend(title="Iris Flowers:")
plt.show()

# Box Plot
male.plot.box()

#notch='True', vert=0
plt.title("Box Plot")
plt.legend(labels=['age','SMOKER','CHILDREN','BMI','REGION'], title="Iris Flowers")

plt.show()

# pairplot
import seaborn as sns
sns.set(style="white")

sns.pairplot(data,hue="sex")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)


def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    """
    Draw a gradient image based on a colormap.

    Parameters
    ----------
    ax : Axes
        The axes to draw on.
    direction : float
        The direction of the gradient. This is a number in
        range 0 (=vertical) to 1 (=horizontal).
    cmap_range : float, float
        The fraction (cmin, cmax) of the colormap that should be
        used for the gradient, where the complete colormap is (0, 1).
    **kwargs
        Other parameters are passed on to `.Axes.imshow()`.
        In particular, *cmap*, *extent*, and *transform* may be useful.
    """
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, interpolation='bicubic', clim=(0, 1),
                   aspect='auto', **kwargs)
    return im


def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))


fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# background image
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()



import matplotlib.pyplot as plt

data = {'male1': 10000, 'female': 5000, 'male2': 5000, 'female2': 2000}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')
plt.show()
