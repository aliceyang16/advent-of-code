# This year is Python!

Python version
```
❯ python3 --version
Python 3.11.6
```

Set up virtual environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create the day's folder, download input data, and setup solve script
```
./get_input.sh
```

Run the solution script
```
python3 day6/solve.py
```

Modify the solve script if you need to change to read a different file
```
input = read_input("day6/input.txt")
```
