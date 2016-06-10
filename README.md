# Testsuite Scrambler

## Usage

1. Install Python 2.7
2. Clone repository `git clone https://github.com/jnehring/testsuite-scrambler`
3. Confiugre scrambler.py
4. Run Skript: python scrambler.py

The skript takes these input files:

| Filename  | Description |
| ------------- |-------------|
| test-items.txt      | File that contains test items with one test item in each line. All test items will be used. |
| distractor.txt      | File that contains distractors. One line per distractor.      |

The skript generates files in the output directory. All filenames have the current date and time attached to the filename, denoted with "123" in these examples:

| Filename  | Description |
| ------------- |-------------|
| secret-123.csv | This is the secret file that should not be shared with others. It is in CSV format, separated by \t. The CSV file contains the columns  |
| distractor-123.txt     | File that contains distractors. One line per distractor. |
| test-items-123.txt | A copy of the test items file used to generate this testsuite |

## Configuration

All configuration options can be done in scrambler.py

### Configuration for scramble

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

### Configuration for unscramble

* No empty lines in the data files
