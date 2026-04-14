# numbers = [1, 2, 2, 3, 3, 3, 4, 5]

# freq = {}

# for num in numbers:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# max_count = 0
# min_count = len(numbers)
# most_frequent = None
# least_frequent = None


# for key in freq:
#     if freq[key] > max_count:
#         max_count = freq[key]
#         most_frequent = key

#     if freq[key] < min_count:
#         min_count = freq[key]
#         least_frequent = key

# print("Most frequent:", most_frequent)
# print("Least frequent:", least_frequent)

from collections import Counter
a="jeevankumar"
b=Counter(a)
print(b)

