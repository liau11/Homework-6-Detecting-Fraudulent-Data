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
    digits = [0.1] * 10
    plt.plot(digits, label="Ideal")
    plt.plot(histogram, label="Iran")
    plt.legend(loc='upper left')
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.savefig("iran-digits.png")
    plt.show()
    plt.clf()

def plot_dist_by_sample_size():
    plt.title("Distribution of last two digits in randomly generated samples")
    digits = [0.1] * 10
    plt.plot(digits, label="Ideal")
    sample_size = [10, 50, 100, 1000, 10000]
    for sample in sample_size:
        dist = [random.randint(1, 99) for i in range(sample)]
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
    print(mean_squared_error)

def calculate_mse_with_uniform(histogram):

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
    mean_squared_error(numbers_1, numbers_2)
    

if __name__ == "__main__":
    main()
