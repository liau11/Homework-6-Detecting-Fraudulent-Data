from sunau import Au_read


# Lily Au
# CSE 160
# HW 6

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

# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    iran_candidates_2009 = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    extract_election_votes("election-iran-2009.csv", iran_candidates_2009)


if __name__ == "__main__":
    main()
