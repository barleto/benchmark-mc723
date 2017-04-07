'''
=================
3D wireframe plot
=================

A very basic demonstration of a wireframe plot.
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import csv
import sys

def subgroup(l,n):
    i=0
    new_list=[]
    while i<len(l):
        new_list.append(l[i:i+n])
        i+=n
    return new_list

with open(sys.argv[1], 'r') as csvfile:
    reader = csv.reader(csvfile)
    table = []
    for row in reader:
        table.append(row)
    table = table[2:]
    sizes = []
    bsizes = []
    dmisses = []
    for row in table:
        sizes.append(int(row[0].replace(" ","").replace("K","")))
        bsizes.append(int(row[1].replace(" ","").replace("K","")))
        dmisses.append(int(row[4].replace(" ","").replace("K","")))
    #sizes = (subgroup(sizes,3))
    #bsizes = (subgroup(bsizes,3))
    #dmisses = (subgroup(dmisses,3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot a basic wireframe.
    #ax.scatter(sizes, bsizes, dmisses)

    ax.set_xlabel('cache size')
    ax.set_ylabel('block size')
    ax.set_zlabel('misses')

    from matplotlib import cm
    cm.coolwarm
    ax.plot_trisurf(sizes, bsizes, dmisses, linewidth=0.2, antialiased=True, cmap=cm.coolwarm)
    #plt.plot(sizes,dmisses)
    fig.savefig("graphs/"+sys.argv[1]+".d.1.png")


with open('gzip.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    table = []
    for row in reader:
        table.append(row)
    table = table[2:]
    sizes = []
    bsizes = []
    dmisses = []
    for row in table:
        sizes.append(int(row[0].replace(" ","").replace("K","")))
        bsizes.append(int(row[2].replace(" ","").replace("K","")))
        dmisses.append(int(row[4].replace(" ","").replace("K","")))
    #sizes = (subgroup(sizes,3))
    #bsizes = (subgroup(bsizes,3))
    #dmisses = (subgroup(dmisses,3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot a basic wireframe.
    #ax.scatter(sizes, bsizes, dmisses)

    ax.set_xlabel('cache size')
    ax.set_ylabel('assoc')
    ax.set_zlabel('cache misses')

    from matplotlib import cm
    cm.coolwarm
    ax.plot_trisurf(sizes, bsizes, dmisses, linewidth=0.2, antialiased=True, cmap=cm.coolwarm)
    #plt.plot(sizes,dmisses)
    fig.savefig("graphs/"+sys.argv[1]+".d.2.png")

with open(sys.argv[1], 'r') as csvfile:
    reader = csv.reader(csvfile)
    table = []
    for row in reader:
        table.append(row)
    table = table[2:]
    sizes = []
    bsizes = []
    dmisses = []
    for row in table:
        sizes.append(int(row[0].replace(" ","").replace("K","")))
        bsizes.append(int(row[1].replace(" ","").replace("K","")))
        dmisses.append(int(row[3].replace(" ","").replace("K","")))
    #sizes = (subgroup(sizes,3))
    #bsizes = (subgroup(bsizes,3))
    #dmisses = (subgroup(dmisses,3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot a basic wireframe.
    #ax.scatter(sizes, bsizes, dmisses)

    ax.set_xlabel('cache size')
    ax.set_ylabel('block size')
    ax.set_zlabel('misses')

    from matplotlib import cm
    cm.coolwarm
    ax.plot_trisurf(sizes, bsizes, dmisses, linewidth=0.2, antialiased=True, cmap=cm.coolwarm)
    #plt.plot(sizes,dmisses)
    fig.savefig("graphs/"+sys.argv[1]+".i.1.png")


with open('gzip.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    table = []
    for row in reader:
        table.append(row)
    table = table[2:]
    sizes = []
    bsizes = []
    dmisses = []
    for row in table:
        sizes.append(int(row[0].replace(" ","").replace("K","")))
        bsizes.append(int(row[2].replace(" ","").replace("K","")))
        dmisses.append(int(row[3].replace(" ","").replace("K","")))
    #sizes = (subgroup(sizes,3))
    #bsizes = (subgroup(bsizes,3))
    #dmisses = (subgroup(dmisses,3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot a basic wireframe.
    #ax.scatter(sizes, bsizes, dmisses)

    ax.set_xlabel('cache size')
    ax.set_ylabel('assoc')
    ax.set_zlabel('cache misses')

    from matplotlib import cm
    cm.coolwarm
    ax.plot_trisurf(sizes, bsizes, dmisses, linewidth=0.2, antialiased=True, cmap=cm.coolwarm)
    #plt.plot(sizes,dmisses)
    fig.savefig("graphs/"+sys.argv[1]+".i.2.png")
