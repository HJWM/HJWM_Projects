# 遗传算法Python求解
# max f(x1,x2) = 21.5 +x1 * sin(4 * PI * x1) + x2 * sin(20 * PI * x2) 求最优解
# 限制范围 -3.0 <=  x1 <= 12.1 , 4.1 <= x2 <= 5.8
# 精度范围：10 ^ -4
import math

import random

from utils import utils


def evolution():
    # 初始种群数量
    N = 10
    M = 10
    E = 2
    cross_probability = 0.6
    mutation_probability = 0.01
    # 获取二进制编码长度
    parameters = {'x1': [-3.0, 12.1], 'x2': [4.1, 5.8]}
    preceision = 4
    lens = utils.encodeLens(parameters, preceision)
    # 产生初始种群
    encode_len = utils.encodeTotalLen(lens)
    population = init_population(N, encode_len)
    for i in range(5000):
        # 后代
        o = []
        # 保留最好的E个直接到下一代种群
        # print(population)
        # best_descent = choose_best_descent(E, population, lens, parameters)
        # o.extend(best_descent)
        # for i in best_descent:
        #     population.remove(i)
        # 计算每个个体的适应度
        fitness = get_fitness(population, lens, parameters)
        # print(fitness)
        # 轮盘赌选择
        probability = roulette(fitness)
        # print(probability)
        # 选择个体
        individual = choose_individual(M, population, probability)
        # print(individual)
        # 交叉
        cross_descent = cross(population, individual, cross_probability)
        # 变异
        mutation_descent = mutation(mutation_probability, cross_descent)
        # print(mutation_descent)
        o.extend(mutation_descent)
        o.extend(cross_descent)
        population.extend(o)
        # 按适应度排序
        population = sort_by_fitness(population, lens, parameters)
        if len(population) > 300:
            population = population[0:300]
        fitness_s = sorted(get_fitness(population, lens, parameters), reverse=True)
        print(fitness_s[0])


def init_population(N, encode_len):
    population = []
    for i in range(N):
        x = ''
        for j in range(encode_len):
            if random.random() > 0.5:
                x += '1'
            else:
                x += '0'
        population.append(x)
    return population


'''
获取适应度
'''


def get_fun_express(*args):
    # print(args)
    return 21.5 + args[0] * math.sin(4 * math.pi * args[0]) + args[1] * math.sin(20 * math.pi * args[1])


def get_fitness(population, lens, range):
    fitness = []
    x1_len = lens['x1']
    x2_len = lens['x2']
    for p in population:
        x1_str = p[0:x1_len]
        x2_str = p[x1_len:x1_len + x2_len]
        x1 = int(x1_str, 2)
        x2 = int(x2_str, 2)
        fitness.append(get_fun_express(utils.decode(x1, range['x1'], x1_len), utils.decode(x2, range['x2'], x2_len)))
    return fitness


def roulette(fitness):
    total = sum(fitness)
    each_fitess_probability = list(map(lambda x: x / total, fitness))
    y = 0
    probability = []
    for x in each_fitess_probability:
        y += x
        probability.append(y)
    return probability


def choose_individual(M, population, probability):
    # M为选择个体的数量
    individual = []
    for i in range(M):
        random_num = random.random()
        for i, val in enumerate(probability):
            if random_num > 0 and random_num <= probability[0]:
                individual.append(0)
                break
            if random_num > val and random_num <= probability[i + 1]:
                individual.append((i + 1))
    return (individual)


def cross(population, individual, cross_probability):
    cross_descent = []
    for i in range(0, int(len(individual)), 2):
        if random.random() < cross_probability:
            cross_point_A = random.randrange(len(population[individual[i]]))
            cross_point_B = random.randrange(len(population[individual[i + 1]]))
            cross_points = sorted([cross_point_B, cross_point_A])
            # print(cross_points)
            offspring_A = population[individual[i]][0:cross_points[0]] \
                          + population[individual[i + 1]][cross_points[0]:cross_points[1]] \
                          + population[individual[i]][cross_points[1]:len(population[individual[i]])]
            offspring_B = population[individual[i + 1]][0:cross_points[0]] \
                          + population[individual[i]][cross_points[0]:cross_points[1]] \
                          + population[individual[i + 1]][cross_points[1]:len(population[individual[i + 1]])]
            # print(offspring_A, offspring_B)
            # 变异
            cross_descent.append(offspring_B)
            cross_descent.append(offspring_A)
    return cross_descent


def mutation(mutation_probability, cross_descent):
    mutation_descent = []
    for indivdual in cross_descent:
        indivdual_list = list(indivdual)
        for i in range(len(indivdual_list)):
            if random.random() > mutation_probability:
                continue
            else:
                if indivdual_list[i] == '0':
                    indivdual_list[i] = '1'
                else:
                    indivdual_list[i] = '0'
                s = ''.join(indivdual_list)
                mutation_descent.append(s)
    return mutation_descent


def choose_best_descent(E, population, lens, parameters):
    indivdual_fitness_dict = {}
    indibdual_best_fitness_list = []
    fitness = get_fitness(population, lens, parameters)
    for i, indivdual_fitness in enumerate(fitness):
        indivdual_fitness_dict[population[i]] = fitness[i]
    for i in range(E):
        indivdual_fitness_l = sorted(indivdual_fitness_dict.items(), key=lambda d: d[1], reverse=True)
        indibdual_best_fitness_list.append(indivdual_fitness_l[i][0])

    return indibdual_best_fitness_list


def sort_by_fitness(population, lens, parameters):
    population_fitness_dict = {}
    population_fitness_list = []
    fitness_list = get_fitness(population, lens, parameters)
    for i in range(len(population)):
        population_fitness_dict[population[i]] = fitness_list[i]
    after_sort_list = sorted(population_fitness_dict.items(), key=lambda d: d[1], reverse=True)
    # print(after_sort_list)
    for x in after_sort_list:
        population_fitness_list.append(x[0])
    return population_fitness_list


evolution()
