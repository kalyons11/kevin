# Quick script to calculate GPA given a class list file.
# Class list file should be a csv with COURSE_ID,NUM_UNITS,GRADE
# GRADE should be LETTER with potential modifiers after that
# registrar.mit.edu/classes-grades-evaluations/grades/calculating-gpa

import argparse
import pandas as pd


def get_parser():
    # Get the argument parser for this script
    parser = argparse.ArgumentParser()
    parser.add_argument('-F', '--filename', help='Filename for grades')
    return parser


class GPACalculator:

    def __init__(self, fname):
        # Load file via pandas
        self.__data = pd.read_csv(
            fname,
            header=None,
            names=['course', 'units', 'grade']
        )

    def calc_gpa(self):
        # Map grades to grade points
        grade_points = self.__data.grade.apply(self.__grade_point_mapper)

        # Multiply pointwise by units
        grade_points_weighted = grade_points * self.__data.units

        # Sum weighted units
        weighted_units_sum = grade_points_weighted.sum()

        # Divide by total units
        gpa_raw = weighted_units_sum / self.__data.units.sum()

        # Round to nearest tenth
        return round(gpa_raw, 1)

    def __grade_point_mapper(self, grade):
        # Maps a string letter grade to a numerical value
        # MIT 5.0 scale
        grade_map = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'F': 0,
        }

        first_char = grade[0].upper()
        try:
            return grade_map[first_char]
        except:
            raise ValueError('Invalid grade {grade}'.format(grade=grade))

if __name__ == '__main__':
    # Set up argument parsing
    parser = get_parser()
    args = parser.parse_args()

    # Make sure filename is present
    if not args.filename:
        raise ValueError('Must provide filename via -F, --filename')

    # Create calculator
    calc = GPACalculator(args.filename)

    # Execute and print
    gpa = calc.calc_gpa()
    print(gpa)
