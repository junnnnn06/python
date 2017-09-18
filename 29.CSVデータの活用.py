'''
CSVデータの活用
1960年から2012年の各年の米国人口の差異の平均値、中央値、分散、標準偏差
'''
import matplotlib.pyplot as plt
import csv
from statistics import mean, median,variance,stdev

def read_csv(filename):

    years = []
    population = []

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        summer = []
        highest_correlated = []
        for row in reader:

            year = row[0].split('-')[0]
            years.append(year)
            population.append(float(row[1]))

    population = population[::-1]
    years = years[::-1]

    return population, years

def plot_population(population, years):

    plt.figure(1)
    xaxis_positions = range(0, len(years))
    plt.plot(population, 'r-')
    plt.title('Total population in US')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(xaxis_positions, years, rotation=45)

def calculate_stats(population):
    growth = []
    for i in range(0, len(population)-1):
        growth.append(population[i+1] - population[i])
    print('Mean growth: {0:.5f}'.format(mean(growth)))
    print('Median growth: {0:.5f}'.format(median(growth)))
    print('Variance/Sd growth: {0:.5f}, {1:.5f}'.format(*variance_sd(growth)))
    return growth

def plot_population_diff(growth, years):

    xaxis_positions = range(0, len(years)-1)
    xaxis_labels = ['{0}-{1}'.format(years[i], years[i+1])
                    for i in range(len(years)-1)]
    plt.figure(2)
    plt.plot(growth, 'r-')
    plt.title('Population Growth in consecutive years')
    plt.ylabel('Population Growth')
    plt.xticks(xaxis_positions, xaxis_labels, rotation=45)

if __name__ == '__main__':
    population, years = read_csv('USA_SP_POP_TOTL.csv')
    plot_population(population, years)
    growth = calculate_stats(population)
    plot_population_diff(growth, years)
    plt.show()
