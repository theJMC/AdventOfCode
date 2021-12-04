
def generate(list):
    zero = 0
    one = 0
    for i in list:
        if int(i) == 0:
            zero += 1
        else:
            one += 1
    return (zero, one)

def getData():
    with open("input.txt", "r") as file:
        lines = [line.rstrip('\n') for line in file]

        fdata = [[],[],[],[],[],[],[],[],[],[],[],[]]

        for i in range(12):
            for line in lines:
                fdata[i].append(line[i])
    return fdata

def main():
    data = getData()
    gamma = []
    for line in data:
        gen = generate(line)
        if gen[0] > gen[1]:
            gamma.append(0)
        else:
            gamma.append(1)

    epsilon = []
    for line in data:
        gen = generate(line)
        if gen[0] < gen[1]:
            epsilon.append(0)
        else:
            epsilon.append(1)

    string_list = [str(int) for int in gamma]
    gamma_dec_list = ''.join(string_list)
    gamma_dec = int(gamma_dec_list, 2)

    string_list = [str(int) for int in epsilon]
    epsilon_dec_list = ''.join(string_list)
    epsilon_dec = int(epsilon_dec_list, 2)

    print(f"Gamma: {gamma_dec}")
    print(f"Epsilon: {epsilon_dec}")
    print(epsilon_dec * gamma_dec)
    

if __name__ == "__main__":
    main()