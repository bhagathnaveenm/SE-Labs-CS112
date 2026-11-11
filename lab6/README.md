# L6_L7_50 — Recycling Rewards

Lab 6: Code and Branch Coverage

## About

A small Python module that works out reward points by material, weight and bonus, checks whether a collection is accepted and reports pickup slot status.

## Files

| File | Description |
|------|-------------|
| `recycling_rewards.py` | The module under test |
| `test_recycling_rewards.py` | Original starter test file |
| `CodeCoverageTest_xxxx_application.py` | Tests for code coverage |
| `BranchCoverageTest_xxxx_application.py` | Tests for branch coverage |
| `CodeCoverage_xxxx_application.png` | Passing code coverage terminal output (100%) |
| `BranchCoverage_xxxx_application.png` | Passing branch coverage terminal output (100%) |
| `Coverage_Report_xxxx_application.pdf` | Coverage analysis, commands, results, and screenshots |

## Run the coverage suites

From the repository root, run each suite independently:

```powershell
python -m pytest -q --cov=recycling_rewards --cov-branch --cov-report=term-missing "Lab 6\CodeCoverageTest_xxxx_application.py"
python -m pytest -q --cov=recycling_rewards --cov-branch --cov-report=term-missing "Lab 6\BranchCoverageTest_xxxx_application.py"
```

Both suites currently achieve 100% statement and branch coverage.

Keep all your Lab 6 work in this `LAB6` folder. Lab 7 will be added to this repo later.

Refer to the lab handout for instructions.
