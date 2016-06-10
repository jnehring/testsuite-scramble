# Testsuite Scrambler

## Usage

1. Install Python 2.7
2. Clone repository `git clone https://github.com/jnehring/testsuite-scrambler`
3. Confiugre scrambler.py
4. Run script: python scrambler.py

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

| Parameter name        | Description           | Example value  |
| ------------- |-------------| -----|
| mode | Define if you want to use the skript for scramble or unscramble. Can be either "scramble" or "unscramble". | "scramble" |
| distractor_file | Path to the file that contains distractors. One line per distractor. | "distractor.txt" |
| test_items_file | Path to the file that contains the test items with one test item in each line. All test items will be used.  | "test-items.txt" |
| number_of_distractors | How many distractors should be used? | 100 |
| translate_test_items | Boolean flag if test items should be translated. | True or false |
| translate_distractors | Boolean flag if distractors should be translated | True or false |
| source_lang | Source language for translation. Only used when translate_test_items=True or translate_distractors=True | "en" |
| target_lang | Target language for translation. Only used when translate_test_items=True or translate_distractors=True | "de" |
| google_api_key | The Google API key used for Google translate. only used when translate_test_items=True or translate_distractors=True | "abcdefg" |

### Configuration for unscramble

| Parameter name        | Description           | Example value  |
| ------------- |-------------| -----|
| secret_file | This is the path to the secret file used as input for unscramble| "output/secret-2016-06-07---10-09-00.csv" |
| translation_file | This is the path to the translation file used as input for unscramble| "output/translation-2016-06-07---10-09-00.txt" |
| outfile | This is the path of the output file of unscramble | "output/uncramble-2016-06-07---10-09-00.csv" |

## Remarks

* No empty lines in the data files.
* You should use a new distractor file. The distractor file provided in this repository is public and therefore the distractors in your scramble file can be identified.
* You can use create-translations.py to generate an example translation file that can be used to test how the script works. After using scramble you can use create-translations.py to generate the translation_file that is the input for unscramble.
