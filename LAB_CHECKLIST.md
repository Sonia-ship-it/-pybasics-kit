# 📋 Lab Submission Checklist: "Create & Publish a Python Package"

Use this interactive checklist to verify every milestone of your lab assignment before final submission.

- [ ] Python installed (Python 3.8+)
- [ ] pip upgraded (`python -m pip install --upgrade pip`)
- [ ] build installed (`python -m pip install build`)
- [ ] twine installed (`python -m pip install twine`)
- [ ] pytest installed (`python -m pip install pytest`)
- [ ] Project structure created (using modern `src/` layout)
- [ ] Python modules implemented (`math_utils.py`, `text_utils.py`, `conv_utils.py`, `game_utils.py`)
- [ ] Tests written (comprehensive test coverage in `tests/`)
- [ ] All tests passing (`python -m pytest -v`)
- [ ] pyproject.toml configured (PEP 621 compliant with setuptools build-backend)
- [ ] Package built successfully (`python -m build`)
- [ ] dist/ contains wheel (`.whl`) and source distribution (`.tar.gz`)
- [ ] TestPyPI account created (registered at https://test.pypi.org)
- [ ] TestPyPI API token created (generated with scope set to Entire Account or Project)
- [ ] Package uploaded to TestPyPI (`python -m twine upload --repository testpypi dist/*`)
- [ ] Package installed from TestPyPI in a fresh environment (`python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pybasics-kit`)
- [ ] Package functions tested and verified in Python REPL / test script
- [ ] GitHub repository created (`git init`, commit, and push to remote)
- [ ] GitHub repository link ready: `https://github.com/Sonia-ship-it/pybasics-kit`
- [ ] TestPyPI package link ready: `https://test.pypi.org/project/pybasics-kit/`
- [ ] Terminal output screenshot captured (showing tests passing, build success, and TestPyPI upload/install)
