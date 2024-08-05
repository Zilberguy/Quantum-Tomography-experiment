import numpy as np

# each bit that is 1 contributes 1 to the number of VV coincidences, and each bit that is 0 contributes 1 to the number of HH coincidences.
# That means that in order to calculate the density matrix from n random bits, we are only interested in the number of 1s in the bit string.
# Because the probability for a 1 is a constant 0.5 for each bit, the number of 1s is a random variable with binomial distribution with p = 0.5.
# So our simulation is simply to generate a random number from a binomial distribution with n trials and p = 0.5.

# this code will generate the csv file of the density matrix

def density_matrix(n):
    random_number = np.random.binomial(n, 0.5)
    density_matrix = np.zeros((4, 4), dtype=float)
    density_matrix[0][0] = (n - random_number) / n
    density_matrix[3][3] = random_number / n
    density_matrix[0][3] = np.sqrt(density_matrix[0][0] * density_matrix[3][3])
    density_matrix[3][0] = np.sqrt(density_matrix[0][0] * density_matrix[3][3])
    np.savetxt(f"simulation_density_matrix_n={n}.csv", density_matrix, delimiter=",")


if __name__ == '__main__':
    lengths = [10, 100, 1000]
    for n in lengths:
        density_matrix(n)
