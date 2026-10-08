# 📋 Lab Submission Checklist: "Create & Publish a Python Package"

Use this interactive checklist to verify every milestone of your lab assignment before final submission.

- [x] Python installed (Python 3.8+)
- [x] pip upgraded (`python -m pip install --upgrade pip`)
- [x] build installed (`python -m pip install build`)
- [x] twine installed (`python -m pip install twine`)
- [x] pytest installed (`python -m pip install pytest`)
- [x] Project structure created (using modern `src/` layout)
- [x] Python modules implemented (`math_utils.py`, `text_utils.py`, `conv_utils.py`, `game_utils.py`)
- [x] Tests written (comprehensive test coverage in `tests/`)
- [x] All tests passing (`python -m pytest -v`)
- [x] pyproject.toml configured (PEP 621 compliant with setuptools build-backend)
- [x] Package built successfully (`python -m build`)
- [x] dist/ contains wheel (`.whl`) and source distribution (`.tar.gz`)
- [x] TestPyPI account created (registered at https://test.pypi.org)
- [x] TestPyPI API token created (generated with scope set to Entire Account or Project)
- [x] Package uploaded to TestPyPI (`python -m twine upload --repository testpypi dist/*`)
- [x] Package installed from TestPyPI in a fresh environment (`python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pybasics-kit`)
- [x] Package functions tested and verified in Python REPL / test script
- [x] GitHub repository created locally (`git init`, commit on branch main)
- [x] GitHub repository link ready: `https://github.com/Sonia-ship-it/-pybasics-kit`
- [x] TestPyPI package link ready: `https://test.pypi.org/project/pybasics-kit/`
- [ ] Terminal output screenshot captured (showing tests passing, build success, and TestPyPI upload/install)
