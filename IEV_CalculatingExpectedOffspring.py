input = '16298 16360 18376 16233 18250 19449'

nums = [int(i) for i in input.split(' ')]
spring_list = [0.75 * nums[3], 0.5 * nums[4]]
for i in range(3):
    spring_list.append(nums[i])

print(sum(spring_list)*2)