# python-starter-2

Introduction to Numerical Analysis

## Requirements

You need to install [`NumPy`](https://numpy.org/) and [`SciPy`](https://scipy.org/). Furthermore, if you want to run "test codes" on your laptop, you will need [`PyTest`](https://pytest.org/) and `PyTest-Timeout`. They can be installed using `pip` (using a virtual environment is recommended but optional):

```bash
# commands may be python3 and pip3 on your system,
python --version  # Check version >= 3.8
pip --version     # Check your pip is for correct Python version

pip install numpy scipy
pip install pytest pytest-timeout
```

## Tasks

- [ ] 5. [Basic Numerics](/task05_basic.md)
- [ ] 6. [NumPy](/task06_numpy.md)
- [ ] 7. [Matrix](/task07_matrix.md)
- [ ] 8. [Newton Method](/task08_newton.md)

Open each `.md` file. Following the instructions, edit `.py` files.

You can edit `.py` files on GitHub, but it is recommended to code on your computer. Following Git/GitHub starter, you are asked to

- **clone** this GitHub repository (*remote repository*) to your computer,
- edit your files on your computer,
- **commit** your changes to the repository in your computer (*local repository*), and
- **push** your local repository to the *remote repository* on GitHub.
- Then, if you can, try **creating a pull request** following [this instruction](/misc/github_pull_request.pdf).

## How to run test codes

Try `python -m pytest` on the root directory of this repository (i.e., where this file is).

If you want to test your code for optional problems, run `python -m pytest --optionial`.

If you want to run a specific test file, you can use `python -m pytest -k tests/test_file_name.py`.

(But test codes may have bugs because you are the first tester of these tests! Please let me know if you find any problems.)
