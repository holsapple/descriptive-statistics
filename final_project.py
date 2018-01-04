""" Intro to Descriptive Statistics - Final Project

This project simulates drawing three cards from a standard deck of cards,
and generates the corresponding sampling distribution.

 - Raymond W. Holsapple
 - last update: Sep 3, 2017

"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# card value order: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
cardvalues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Spades (1-13), Diamonds (14-26), Clubs (27-39), Hearts (40-52)
valuemap = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 10, 12: 10, 13: 10,
            14: 1, 15: 2, 16: 3, 17: 4, 18: 5, 19: 6, 20: 7, 21: 8, 22: 9, 23: 10, 24: 10, 25: 10, 26: 10,
            27: 1, 28: 2, 29: 3, 30: 4, 31: 5, 32: 6, 33: 7, 34: 8, 35: 9, 36: 10, 37: 10, 38: 10, 39: 10,
            40: 1, 41: 2, 42: 3, 43: 4, 44: 5, 45: 6, 46: 7, 47: 8, 48: 9, 49: 10, 50: 10, 51: 10, 52: 10}
generate_figs = False


def drawcards(n):
    draw = np.random.choice(np.arange(1, 53), size=n, replace=False)
    return sum([valuemap[card] for card in draw])


def popdistribution():
    pophistvalues = []
    pophistbins = np.arange(2, 31) + 0.5
    for i in np.arange(1, 51):
        for j in np.arange(i+1, 52):
            for k in np.arange(j+1, 53):
                pophistvalues.append(sum([valuemap[i], valuemap[j], valuemap[k]]))
    populationdist = np.histogram(pophistvalues, bins=np.arange(3, 31))
    mu = np.mean(pophistvalues)
    popmed = np.median(pophistvalues)
    sigma = np.std(pophistvalues)
    print()
    print('The mean of the population is', mu)
    print('The median of the population is', popmed)
    print('The population standard deviation is', sigma)
    print()
    if generate_figs:
        plt.figure()
        plt.hist(pophistvalues, pophistbins, normed=1, edgecolor='black', linewidth=0.5, facecolor='red')
        plt.xlabel('3-Card Draw Value')
        plt.ylabel('Relative Frequency')
        plt.title('3-Card Draw Experiment Histogram')
        plt.xticks(np.arange(3, 31), fontsize=6)
        plt.savefig('population_distribution.png', dpi=1000)
    return populationdist


def meansampdist(n, numberdraws, numberexperiments):
    samplemeans = []
    for k in range(n):
        sample = []
        for j in range(numberexperiments):
            sample.append(drawcards(numberdraws))
        samplemeans.append(np.mean(sample))
    meanofmeans = np.mean(samplemeans)
    stdofmeans = np.std(samplemeans, ddof=1)
    print()
    print('The mean of the sample means is', meanofmeans)
    print('The standard deviation of the sample means is', stdofmeans)
    print()
    if generate_figs:
        plt.figure()
        plt.hist(samplemeans, bins='auto', normed=1, edgecolor='black', linewidth=0.5, facecolor='blue')
        plt.xlabel('Sample Mean')
        plt.ylabel('Relative Frequency')
        plt.title('Sampling Distribution of Sample Means')
        plt.savefig('sampling_dist_sample_means.png', dpi=1000)
    return meanofmeans, stdofmeans

if __name__ == '__main__':

    # 1. First, create a histogram depicting the relative frequencies of the card values.
    histvalues = cardvalues * 4
    histbins = np.arange(11) + 0.5
    if generate_figs:
        plt.figure()
        plt.hist(cardvalues, histbins, normed=1, edgecolor='black', linewidth=0.5, facecolor='green')
        plt.xlabel('Card Value')
        plt.ylabel('Relative Frequency')
        plt.title('Card Value Histogram')
        plt.xticks(np.arange(1, 11))
        plt.savefig('card_values_hist.png', dpi=1000)
    # Comment the line below if you don't want the population histogram and parameters.
    populationdist = popdistribution()

    # 2. Now, we will get samples for a new distribution. To obtain a single sample, shuffle your deck of cards and draw
    # three cards from it. (You will be sampling from the deck without replacement.) Record the cards that you have drawn
    # and the sum of the three cards’ values. Replace the drawn cards back into the deck and repeat this sampling procedure
    # a total of at least thirty times.
    numdraws = 3
    numexpinsample = 30
    sample = []
    for k in range(numexpinsample):
        sample.append(drawcards(numdraws))

    # 3. Let’s take a look at the distribution of the card sums. Report descriptive statistics for the samples you have drawn.
    # Include at least two measures of central tendency and two measures of variability.
    samplemean = np.mean(sample)
    samplemedian = np.median(sample)
    samplestd = np.std(sample, ddof=1)
    samplesem = stats.sem(sample)
    print()
    print('The mean of the sample is', samplemean)
    print('The median of the sample is', samplemedian)
    print('The sample standard deviation is', samplestd)
    print('The standard error of the mean is', samplesem)
    print()

    # 4. Create a histogram of the sampled card sums you have recorded. Compare its shape to that of the original distribution.
    # How are they different, and can you explain why this is the case?
    # print(sample)
    samplebins = np.arange(2, 31) + 0.5
    if generate_figs:
        plt.figure()
        plt.hist(sample, samplebins, normed=1, edgecolor='black', linewidth=0.5, facecolor='purple')
        plt.xlabel('3-Card Draw Value')
        plt.ylabel('Relative Frequency')
        plt.title('3-Card Draw Sample Histogram')
        plt.xticks(np.arange(3, 31), fontsize=6)
        plt.savefig('sample_distribution.png', dpi=1000)
    # Comment the line below if you don't want to simulate a sampling distribution of the mean.
    meanofmeans, stdofmeans = meansampdist(50, numdraws, numexpinsample)

    # 5. Make some estimates about values you will get on future draws.
    # Within what range will you expect approximately 90% of your draw values to fall? (<--- I think this question is ambiguous or should be worded better.)
    # What is the approximate probability that you will get a draw value of at least 20? Make sure you justify how you obtained your values.
    # I'm going to approach this part of the project in two ways. First, I am going to answer the question as if we are talking about probabilities
    # regarding the mean of a sample the same size as I chose in the variable 'numexpinsample'. The sampling distribution of sample means will be approximately
    # normally distributed, but the underlying distribution will not be. As the problem is worded it seems to me as if it is asking to make inferences about
    # a single draw of 3 cards, which is a sample of size 1. To answer the questions from that perspective, we need to use the actual distribution of the
    # experiment or at least use an approximation to that distribution by performing the experiment many times. I have computed the actual discreet distribution
    # so I will use that to answer the questions as well.
    leftz = stats.norm.ppf(0.05)
    rightz = -leftz
    lower90lim = (leftz * stdofmeans) + meanofmeans
    upper90lim = (rightz * stdofmeans) + meanofmeans
    print()
    print('The probability that the mean of a sample of size', numexpinsample, 'will be between', lower90lim, 'and', upper90lim, 'is 0.9 or 90%')
    z20 = (20 - meanofmeans) / stdofmeans
    prob_atleast_20 = 1 - stats.norm.cdf(z20)
    print('The probability that the mean of a sample of size', numexpinsample, 'will be at least 20 is', prob_atleast_20)
    print()
    draw_prob_atleast_20 = sum(populationdist[0][16::])/sum(populationdist[0])
    print('The probability that a single draw of 3 cards will result in a sum of at least 20 is', draw_prob_atleast_20)