# INFO 2950 source

# Repo organization

* Blank homework files (for upload) should be put in `hws/hw[NUMBER]`.
* Homework solutions should be put in `hws/solns/hw[NUMBER]soln`.
* The student solutions folder downloaded from CMS and unzipped as `Submissions` folder) should be put in `grading/hw[NUMBER]/`.

# Auto problem splitting

A Jupyter notebook is actually just a JSON file. The file has an attribute `cells` with a list of cell objects that contain the source and output of a cell. Each cell also contains a `metadata` object. I've added an attribute `problem` to the cell metadata for problem headers. This will not be visible to the students. To edit cell metadata from a notebook, use View > Cell Toolbar > Edit Metadata. Each cell will then have an "edit metadata" bar along the top, which allows you to edit the raw JSON of the `metadata` object.

## Creating homework

To make creating a new homework with the right cell metadata easy there is a file `template/homework.ipynb` that has a blank template with headers for 16 problems. Copy the template to a new homework and use however many problem headers you need, deleting any extra. If you need to create more than 16, copy the template problems but make sure to modify the metadata to increment the `problem` attribute. Feel free to modify the format of the template.

## Splitting submissions

If CMS is set for students to upload a single `.ipynb` file, we will be able to download a `zip` file containing one directory called `Submissions` that contains one directory for each registered netid. If a student has turned in a file, that file will appear with the filename specified in CMS (regardless of what they called it) in the directory for the student's netid.

The script reads all the student submission files, identifying the problem breaks by looking for cells with the `problem` attribute. All cells *after* a problem-marker cell and *before* the next problem-marker cell or the end of the notebook are copied to a new notebook specific to that problem. Students should therefore be guided to not add any text to the problem-marker cells.

The inputs to the script are therefore the path to the `Submissions` directory, the standard name of the notebook file (eg `hw5.ipynb`), and the path to write problem-specific notebooks.

Example:

    `python scripts/divide_problems.py sample/Submissions sample.ipynb sample`

This splits the two notebooks from users `dm655` and `ip98` into two problem-specific notebook files, `sample/problem_1.ipynb` and `sample/problem_1.ipynb`.

## Shell script for splitting submissions

You can also split the hws using `split.sh`. Here's an example of how to use it for hw0.

1. Download the `Submissions` folder from CMS, and place it in `grading/hw0/`.
2. Run the following command from the main repo directory: `./split hw0`.
3. The individual problem files will be found in `grading/hw0/subs-split`.
