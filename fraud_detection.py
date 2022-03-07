# Lily Au
# CSE 160
# HW 6


from sunau import Au_read
import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import csv
# Your Set of Functions for this assignment goes in here

def extract_election_votes(filename, column_names):
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
    frequency = []
    for i in range(10):
        frequency.append(0)
        for num in numbers:
            if (num // 10) % 10 == i:
                frequency[i] += 1
            if num % 10 == i:
                frequency[i] += 1
        frequency[i] = frequency[i] / (2 * len(numbers))
    print(frequency)




# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    iran_candidates_2009 = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    num_votes_list = extract_election_votes("election-iran-2009.csv", iran_candidates_2009)
    ones_and_tens_digit_histogram(num_votes_list)

if __name__ == "__main__":
    main()
