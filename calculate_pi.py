import math
import random
import numpy as np
from bokeh.plotting import figure, show
from progress.bar import Bar


def graph(points_inside, points_outside):
    fig = figure()

    for x, y in points_inside:
        fig.asterisk(x, y, size=5, color="red", alpha=0.5)

    for x, y in points_outside:
        fig.asterisk(x, y, size=5, color="blue", alpha=0.5)

    show(fig)


def throw_needles(quantify, create_chart=False):
    needles_inside = needles_outside = []

    needles_bar = Bar('Tirando agujas', max=quantify)
    for _ in range(quantify):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])

        distance_from_center = math.sqrt(x ** 2 + y ** 2)

        if distance_from_center <= 1:
            needles_inside.append((x, y))
        else:
            needles_outside.append((x, y))

        needles_bar.next()

    if create_chart:
        graph(needles_inside, needles_outside)

    needles_bar.finish()

    return (4 * len(needles_inside)) / quantify


def generate_estimates(quantify_needles, quantity_intents):
    estimates = []

    for _ in range(quantity_intents):
        result_estimate = throw_needles(quantify_needles)
        estimates.append(result_estimate)

    avg = np.average(estimates)
    std = np.std(estimates)

    print(estimates)
    print(f'media={avg}')
    print(f'stdev={std}')
    print(f'needles={quantify_needles}')
    print('=' * 50)

    return std


def estimate_pi(precision, quantify_intents):
    quantify_needles = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        sigma = generate_estimates(quantify_needles, quantify_intents)
        quantify_needles *= 2
