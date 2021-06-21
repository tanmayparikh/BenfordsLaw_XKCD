import re
import math
import matplotlib.pyplot as plt

with open('descriptions.txt', 'r', encoding='utf-8') as infile:
    data = infile.readlines()

allData = ''.join(data)
allData = allData.replace('\n', '')
allData = allData.replace(',', '')

nums = re.findall('-?\d+\.?\d+', allData)

def first_digit(num):
    return num // 10 ** (int(math.log(num, 10)))

bins = {}
for n in nums:
    try:
        num = int(n)
        num = abs(num)
        firstDigit = first_digit(num)

        if firstDigit in bins.keys():
            bins[firstDigit] += 1
        else:
            bins[firstDigit] = 1

    except Exception:
        continue

print(f"{len(nums)} numbers found!")

ref_xs = list(range(1, 10))
ref_ys = [math.log10(1 + (1/x)) for x in range(1, 10)]
dat_ys = [bins[x]/len(nums) for x in range(1, 10)]

plt.plot(ref_xs, ref_ys, label="reference")
plt.plot(ref_xs, dat_ys, label="data")
plt.legend()
plt.show()