## Split all hw submissions into problem-specific jupyter notebooks
## input argument 1: CMS filename for hw, without extension (e.g. hw0)

## where are the submissions relative to the home directory?
SOURCEDIRNAME=grading/$1/Submissions
## where should the split submissions be saved?
SPLITDIRNAME=grading/$1/subs-split

if !([ -d $SPLITDIRNAME ])
then
  mkdir $SPLITDIRNAME
fi

python scripts/divide_problems.py $SOURCEDIRNAME $1.ipynb $SPLITDIRNAME
