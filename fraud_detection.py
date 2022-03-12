# Lily Au
# CSE 160
# HW 6

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

    Extracts the strings from specific columns from every row of
    file and removing the "," and turning the string into an integar.
    """
    f = open(filename)
    input_file = csv.DictReader(f)

    votes = []
    for row in input_file:
        for name in column_names:
            col_value = row[name]
            if len(col_value) > 0:
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
        if len(numbers) > 0:
            for num in numbers:
                if (num // 10) % 10 == i:
                    frequency[i] += 1
                if num % 10 == i:
                    frequency[i] += 1
            frequency[i] = frequency[i] / (2 * len(numbers))
    return frequency


def plot_iran_least_digits_histogram(histogram):
    """
    Input:
        histogram - a list of integars created by
        ones_and_tens_digit_histogram
    Output:
        Function does not return anything. It outputs and saves
        the plot to a png file.
    """
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
    """
    Plots the digit histograms for five different collections of random numbers
    on to one graph. Function produces a png file.
    """
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


def larger_count(country_mse, country_data):
    """
    Input:
        country_mse: mse of the country in interest calculated from
        calculate_mse_with_uniform

        country_datapoints - a list of votes from the election of
        the country in interest
    Output:
        returns larger_count
    """
    larger_count = 0
    for i in range(10000):
        rand_data = generate_random_nums(len(country_data))
        histogram = ones_and_tens_digit_histogram(rand_data)
        mse = calculate_mse_with_uniform(histogram)
        if mse >= country_mse:
            larger_count += 1
    return larger_count


def get_p_value(larger_count):
    """
    Input:
        larger_count - number of random MSEs that are larger than or equal
        the country's MSE
    Output:
        Returns p_value
    """
    p_value = larger_count / 10000
    return p_value


def smaller_count(larger):
    """
    Input:
        larger = number of random MSEs that are larger than or equal
        the country's MSE
    Output:
        Returns smaller (number of random MSEs that are smaller)
    """
    smaller = 10000 - larger
    return smaller


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    """
    Input:
        iran_mse - mse of Iran calculated from calculate_mse_with_uniform
        number_of_iran_datapoints - a list of votes from the Iran election
    Output:
        Prints out statistics and p_value for the Iraian election
    """
    larger = larger_count(iran_mse, number_of_iran_datapoints)
    p_value = get_p_value(larger)
    smaller = smaller_count(larger)
    print("2009 Iranian election MSE:", iran_mse)
    print(f"Quantity of MSEs larger than or equal to the 2009 "
          f"Iranian election MSE: {larger}")
    print(f"Quantity of MSEs smaller than the 2009 "
          f"Iranian election MSE: {smaller}")
    print(f"2009 Iranian election null hypothesis rejection "
          f"level p: {p_value}")
    print()


def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    """
    Input:
        us_mse - mse of US calculated from calculate_mse_with_uniform
        number_of_us_datapoints - a list of votes from the US election
    Output:
        Prints out statistics and p_value for the US election
    """
    larger = larger_count(us_mse, number_of_us_datapoints)
    p_value = get_p_value(larger)
    smaller = smaller_count(larger)
    print("2008 United States election MSE:", us_mse)
    print(f"Quantity of MSEs larger than or equal to the 2008 United "
          f"States election MSE: {larger}")
    print(f"Quantity of MSEs smaller than the 2008 United States "
          f"election MSE: {smaller}")
    print(f"2008 United States election null hypothesis rejection "
          f"level p: {p_value}")


# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    iran_cand = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    iran_votes = extract_election_votes("election-iran-2009.csv", iran_cand)
    iran_histogram = ones_and_tens_digit_histogram(iran_votes)
    plot_iran_least_digits_histogram(iran_histogram)
    plot_dist_by_sample_size()
    iran_mse = calculate_mse_with_uniform(iran_histogram)
    compare_iran_mse_to_samples(iran_mse, iran_votes)

    us_2008_cand = ["Obama", "McCain", "Nader", "Barr",
                    "Baldwin", "McKinney"]
    us_votes_lst = extract_election_votes("election-us-2008.csv", us_2008_cand)
    us_histogram = ones_and_tens_digit_histogram(us_votes_lst)
    us_mse = calculate_mse_with_uniform(us_histogram)
    compare_us_mse_to_samples(us_mse, us_votes_lst)


if __name__ == "__main__":
    main()
