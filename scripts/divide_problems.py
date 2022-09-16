import sys, json, glob
from os import path

if len(sys.argv) != 4:
    print("Usage: divide_problems.py PATH/TO/Submissions FILENAME.ipynb PATH/TO/OUTPUT")
    sys.exit()

submissions_dir = sys.argv[1]
ipynb_name = sys.argv[2]
output_dir = sys.argv[3]

## We are constructing a list, where each element represents one problem.
## The element for a problem is a map from netids to lists of cells
## structure: { 1: { "dm655": [...], "ip98": [...] }, 2: { "dm655": [...], ... } }

problem_student_cells = {}
missing_sub_emails = []

def make_notebook(cells):
    notebook = json.loads("""{"metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.7.6"}}, "nbformat": 4, "nbformat_minor": 4}""")
    notebook["cells"] = cells
    return notebook

def make_netid_header(netid):
    return {"cell_type": "markdown", "metadata": {}, "source": ["## {}".format(netid)]}

for student_dir in glob.glob("{}/*".format(submissions_dir)):
    filename = "{}/{}".format(student_dir, ipynb_name)


    netid = path.basename(student_dir)
    print(netid)

    if path.exists(filename):
        with open(filename) as reader:
            try:
                notebook_json = json.load(reader)
                problem_id = None
                for cell in notebook_json["cells"]:
                    if "problem" in cell["metadata"]:
                        problem_id = cell["metadata"]["problem"]
                        # is this the first time we have seen this problem?
                        if not problem_id in problem_student_cells:
                            problem_student_cells[problem_id] = {}
                        # allocate an empty list for cells
                        problem_student_cells[problem_id][netid] = []
                    elif "narrative" in cell["metadata"]:
                        # ignore cells with the attribute "narrative"
                        continue
                    elif problem_id != None:
                        # if we are in a problem (ie not the header), save cells
                        problem_student_cells[problem_id][netid].append(cell)
            except:
                print("{} unable to read file".format(netid))
    else:
        print("{} missing".format(netid))
        missing_sub_emails.append("{}@cornell.edu".format(netid))


for problem_id in sorted(problem_student_cells.keys()):
    student_cells = problem_student_cells[problem_id]
    cells = []

    sorted_netids = sorted(student_cells.keys())
    for netid in sorted_netids:
        cells.append(make_netid_header(netid))
        cells.extend(student_cells[netid])

    with open("{}/problem_{}.ipynb".format(output_dir, problem_id), "w") as writer:
        writer.write(json.dumps(make_notebook(cells)))

## print emails of those with missing submissions
print("\nemails of those missing submissions:\n")
sep = "; "
print(sep.join(missing_sub_emails))
print("\n")
