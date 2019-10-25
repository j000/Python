#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 11.2
QuickSort z grafiką
Jarosław Rymut
"""

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    print()
    print('/!\\ Matplotlib is needed for visualization /!\\')
    print()
    raise

########################################

step = 0

def prepare_plot(A, lo=0, hi=0, pivot=None):
    plt.figure(figsize=(8, 6))
    plt.ylim(-0.5, len(A) + 1.5)
    plt.xlim(-0.5, len(A) + 0.5)
    if lo != hi:
        plt.axvspan(lo - 0.5, hi + 0.5, alpha=0.7, color='yellow')
    if pivot is not None:
        plt.axhline(pivot, alpha=0.7, color='red')
    plt.bar(
        range(len(tmp)),
        [i + 1 for i in tmp],
        color='grey',
        bottom=-1
    )

def finish_plot(*, title=True):
    global step
    if title:
        plt.title(f'Step {step:04d}')
    else:
        plt.title(' ')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'quicksort{step:04d}.png')
    plt.close()
    step += 1

########################################

def visualize(A):
    from collections import deque
    queue = deque()
    queue.appendleft((0, len(A) - 1))
    while queue:
        (lo, hi) = queue.popleft()
        if lo < hi:
            p = visualize_partition(A, lo, hi)
            queue.appendleft((p + 1, hi))
            queue.appendleft((lo, p))
    prepare_plot(A)
    finish_plot(title=False)

def visualize_partition(A, lo, hi):
    global step
    # pivot = A[lo + (hi - lo) // 2]
    pivot = sorted([A[lo], A[lo + (hi - lo) // 2], A[hi]])[1]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        j -= 1
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i >= j:
            return j

        prepare_plot(A, lo, hi, pivot)
        plt.scatter([i, j], [A[i], A[j]], marker='v', color='blue', zorder=10)
        finish_plot()

        A[i], A[j] = A[j], A[i]

########################################

if __name__ == '__main__':
    from generators import *
    tmp = list(random_order(90))

    print(', '.join(map(str, tmp)))
    visualize(tmp)
    print(', '.join(map(str, tmp)))

    import os
    os.system('ffmpeg '\
    '-hide_banner -loglevel error -nostats '\
    '-r 2 -i "quicksort%04d.png" '\
    '-vcodec h264 -an -strict -2 -r 30 -tune animation -pix_fmt yuv420p '\
    '-y quicksort.mp4');
    os.system('rm quicksort????.png')

