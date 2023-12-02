#!/bin/zsh

# Creates the day's folder, downloads the input, and creates some boilerplate code to get started

YEAR=$(date +%Y)
DAY=$(echo $(date +%d) | sed 's/^0*//')
if [[ -n $1 ]]; then
    DAY=$1
fi

SESSION=$(cat .session)

FOLDER="day${DAY}"
BASE_URL="https://adventofcode.com/${YEAR}/day/${DAY}"

mkdir -p $FOLDER
curl -fsSL --cookie session=${SESSION} "${BASE_URL}/input" -o "${FOLDER}/input"

if [[ ! -e ${FOLDER}/solve.py ]]; then
# Generate Python boilerplate if not exists
read -r -d '' template <<-'EOF'
import sys
sys.path.insert(0, '.')
from util.read_input import read_input

# input = read_input("$FOLDER/sample")
input = read_input("$FOLDER/input")

EOF

SOLVE_SCRIPT=$(echo "${template//\$FOLDER/$FOLDER}")

echo "${SOLVE_SCRIPT}" > ${FOLDER}/solve.py
fi
