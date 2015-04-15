import os
from linear_regression import *
dir = ['2001-2002', '2003-2004', '2005-2006', '2007-2008', '2009-2010', '2011-2012']
def get_prob(year_ind, topic_ind):
    fp = open(os.path.join(dir[year_ind], dir[year_ind] + '.theta'))
    prob_sum = 0.0
    for line in fp:
        line = line.strip()
        cur_doc_prob = float(line.split()[topic_ind])
        prob_sum += cur_doc_prob
    return prob_sum

real_topic =[
        [1, 2, 3, 4, 9, 5, 3, 2, 3, 3],
        [3, 9, 6, 2, 3, 3, 3, 6, 1, 5],
        [7, 6, 5, 2, 2, 6, 3, 1, 3, 8],
        [8, 3, 6, 1, 4, 5, 9, 2, 3, 3],
        [3, 10, 1, 3, 5, 5, 5, 3, 9, 2],
        [1, 6, 2, 5, 1, 11, 3, 1, 12, 3]
]

def get_real_topic(year_ind, topic_ind):
    return real_topic[year_ind][topic_ind]
if __name__ == '__main__':
    #print get_prob(0, 0)
    temp_data = [[] for i in range(12)]
    data = [[] for i in range(12)]
    for i in range(12):
        temp_data[i] = [0.0 for j in range(6)]
    for topic_ind in range(10):
        for year_ind in range(6):
            prob_sum = get_prob(year_ind, topic_ind)
            temp_data[get_real_topic(year_ind, topic_ind) - 1][year_ind] += prob_sum
    for i in range(12):
        data[i] = [(j, temp_data[i][j]) for j in range(6)]
    for i in range(9):
        linRegr = SimpleLinearRegression(data[i])
        #print data[i]
        if not linRegr.run():
            print("...error: failed to calculate parameters")

        print("...the coefficient of correlation r = %f (r**2 is %f)" % (linRegr.r, linRegr.r**2))
        #print("...parameter a of y = f(x) = a + b*x is %f" % linRegr.a)
        #print("...parameter b of y = f(x) = a + b*x is %f" % linRegr.b)
        #print("...linear function is then %s" % linRegr)
        print("...forecast of next value: f(6) = %f" % linRegr.function(6))

        firstY = linRegr.function(1)
        lastY  = linRegr.function(4)
        change = (lastY - firstY) / firstY * 100.0

        # keep in mind: reducing of error rate (inverse valuation)!
        if change < 0:
            print("...the trend is about %.1f%% improvement" % -change)
        else:
            print("...the trend is about %.1f%% to the worse" % change)
            #print data


