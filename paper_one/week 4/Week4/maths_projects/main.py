# import study.variable_equation as variable_equation
# from study import funtions
# from study import graph
from study import variance, stdvarience, probability

# # value = variable_equation.house_price(1500)
# # print("Eq and Va", value)

# # output = funtions.f(4)
# # print("f(x) = ", output)

# # mark = [10, 20, 30, 40, 50, 60]
# # time = [0, 1, 2, 3, 4, 5]
# # graph.liner(mark, time)

# ages = [18, 12, 15, 20, 22, 26]

# result = variance.varian(ages)

# print(f"{result:.2f}")

# result_std = stdvarience.std(ages)

# print(f"{result_std:.2f}")

result_prob = probability.prob(1, 6)

print(f"{result_prob:.2f}")

inputdata = {"red": 20, "black": 15, "blue": 10}

# dict_result = probability.prob_dict(inputdata)