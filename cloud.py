import numpy
import boto3
import matplotlib.pyplot as plt
client = boto3.client('ec2',region_name='us-east-1')
machine_types = ["t2.micro", "t2.small", "t2.medium", "c4.large", "m4.large",  "c5.large", "m5.large", "c4.xlarge", "m4.xlarge", "c5.xlarge", "t2.2xlarge", "m5.2xlarge"]
stand_dev = list()
for i in machine_types:
    temp_prices = client.describe_spot_price_history(InstanceTypes=[i], StartTime='2018-08-10T21:14:000Z', EndTime='2018-08-13T21:14:000Z')
    #print(temp_prices)
    try:
        a = [float(i['SpotPrice']) for i in temp_prices['SpotPriceHistory']]
        plt.plot(a)
        plt.xlabel('Over time')
        plt.ylabel('Price')
        plt.title('Price Fluctuations for '+i)
        plt.show()
        print(a)
        stand_dev.append(float(numpy.std(a)))
    except:
        stand_dev.append(0.0)
plt.plot(machine_types, stand_dev)
plt.xlabel('Machine Types')
plt.ylabel('Standard Deviation')
plt.title('Figure 1. Fluctuating Standard Deviation with various Instance types')
plt.show()
user_input = input("Type of machine required: ")
print(stand_dev, machine_types[stand_dev.index(min(stand_dev[machine_types.index(user_input):]))], sep='\n')
