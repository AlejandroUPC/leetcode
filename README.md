# LeetCode Solutions (Python)

This repo contains my LeetCode solutions in Python. Each problem lives in its own folder:

```
exercises/001-two-sum/
  README.md
  main.py
  test.py   # optional
```

## Conventions
- Folder names: `NNN-slug` (zero-padded id + problem slug)
- `main.py`: solution
- `test.py`: quick sanity tests (optional)
- `README.md`: problem notes, approach, and complexity

## Running
From a problem folder:

```bash
cd exercises/001-two-sum
python main.py
python test.py
```

## Makefile
Create a new exercise from the template:

```bash
make new 001-two-sum
```

Create a new pattern folder:

```bash
make newp two-pointer
```

Run all `test.py` files:

```bash
make tests
```
