# Lily Au
# CSE 160
# HW 6


from sunau import Au_read
from importlib_metadata import distribution
import matplotlib.pyplot as plt
import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import csv
import random
# Your Set of Functions for this assignment goes in here

def extract_election_votes(filename, column_names):
    """
    Input:
        filename - name of the file of the data
        column_names - a list of column names
    Output:
        Returns a list of integars from the columns from every row
    """
    f = open(filename)
    input_file = csv.DictReader(f)

    votes = []
    for row in input_file:
        for name in column_names:
            col_value = row[name]
            col_value = col_value.replace(",", "")
            votes.append(int(col_value))
    f.close()
    return votes

def ones_and_tens_digit_histogram(numbers):
    """
    Input: A list of integars
    Output: Returns a list of integars
    
    Finding the frequency of digits found in ones place and tens place
    by pooling the digits and then dividing by the total number of digits
    we looked at
    """
    frequency = []
    for i in range(10):
        frequency.append(0)
        for num in numbers:
            if (num // 10) % 10 == i:
                frequency[i] += 1
            if num % 10 == i:
                frequency[i] += 1
        frequency[i] = frequency[i] / (2 * len(numbers))
    return frequency

def plot_iran_least_digits_histogram(histogram):
    plt.title("Distribution of the last two digits in Iranian dataset")
    uniform_dist = [0.1] * 10
    plt.plot(uniform_dist, label="Ideal")
    plt.plot(histogram, label="Iran")
    plt.legend(loc='upper left')
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.savefig("iran-digits.png")
    plt.show()
    plt.clf()

def generate_random_nums(size):
    """
    Input: 
        size - size of sample
    Output: 
        Returns a list of randoms from 0 - 99
     """
    rand_num_list = [random.randint(1, 99) for i in range(size)]
    return rand_num_list

def plot_dist_by_sample_size():
    plt.title("Distribution of last two digits in randomly generated samples")
    uniform_dist = [0.1] * 10
    plt.plot(uniform_dist, label="Ideal")
    sample_size = [10, 50, 100, 1000, 10000]
    for sample in sample_size:
        dist = generate_random_nums(sample)
        frequency = ones_and_tens_digit_histogram(dist)
        sample_label = str(sample) + " random letters"
        plt.plot(frequency, label=sample_label)
    plt.legend(loc='upper left')
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.savefig("random-digits.png")
    plt.show()
    plt.clf()

def mean_squared_error(numbers1, numbers2):
    """
    Input:
        numbers1: list of numbers
        numbers2: list of numbers
    Output:
        Returns the mean squared error between the two lists
    """
    running_squared_sum = 0
    for i in range(len(numbers1)):
        running_squared_sum += (numbers1[i] - numbers2[i]) ** 2
    mean_squared_error = running_squared_sum / len(numbers1)
    return(mean_squared_error)

def calculate_mse_with_uniform(histogram):
    """
    Input: Histogram created by ones_and_tens_digit_histogram function
    Output: Returns the mean squared error of the given histogram
    """
    uniform_dist = [0.1] * 10
    return (mean_squared_error(histogram, uniform_dist))

def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    """
    Input: 
        iran_mse 
        number_of_iran_datapoints
    """
    larger_count = 0
    smaller_count = 0
    for i in range(10000):
        rand_data = generate_random_nums(len(number_of_iran_datapoints))
        mse = calculate_mse_with_uniform(ones_and_tens_digit_histogram(rand_data))
        if mse >= iran_mse:
            larger_count += 1
        else:
            smaller_count += 1
    p_value = larger_count / 10000
    print("2009 Iranian election MSE:", iran_mse )
    print("Quantity of MSEs larger than or equal to the 2009 Iranian election MSE:", larger_count)
    print("Quantity of MSEs smaller than the 2009 Iranian election MSE:", smaller_count)
    print("2009 Iranian election null hypothesis rejection level p:", p_value)


# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    iran_candidates_2009 = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    num_votes_list = extract_election_votes("election-iran-2009.csv", iran_candidates_2009)
    histogram = ones_and_tens_digit_histogram(num_votes_list)
    plot_iran_least_digits_histogram(histogram)
    plot_dist_by_sample_size()
    mse = calculate_mse_with_uniform(histogram)
    compare_iran_mse_to_samples(mse, num_votes_list)
    

if __name__ == "__main__":
    main()
