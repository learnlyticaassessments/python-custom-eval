import os
import pandas as pd
import numpy as np
import pytest
from assignments.assignment2 import read_data, get_average_salary, get_department_counts, get_top_earners

# Sample data for testing; normally, you might use a temporary CSV file.
TEST_CSV_CONTENT = """Name,Department,Salary,JoiningDate
Alice,HR,50000,2020-01-15
Bob,Engineering,70000,2019-06-01
Charlie,Engineering,65000,2021-03-20
Diana,Marketing,55000,2018-11-30
"""

# Fixture to create a temporary CSV file for testing read_data.
@pytest.fixture
def sample_csv(tmp_path):
    csv_file = tmp_path / "employees.csv"
    csv_file.write_text(TEST_CSV_CONTENT)
    return str(csv_file)

def test_read_data(sample_csv):
    # Test function 1: read_data should return a DataFrame with the correct columns.
    df = read_data(sample_csv)
    assert isinstance(df, pd.DataFrame), "read_data should return a DataFrame."
    expected_columns = {"Name", "Department", "Salary", "JoiningDate"}
    assert expected_columns.issubset(set(df.columns)), f"DataFrame must contain columns {expected_columns}."

def test_get_average_salary(sample_csv):
    # Test function 2: get_average_salary should compute the correct average.
    df = pd.read_csv(sample_csv)
    avg = get_average_salary(df)
    expected_avg = np.mean([50000, 70000, 65000, 55000])
    # Allow a small tolerance for float comparison.
    assert abs(avg - expected_avg) < 1e-6, f"Expected average salary {expected_avg}, got {avg}."

def test_get_department_counts(sample_csv):
    # Test function 3: get_department_counts should return the correct count per department.
    df = pd.read_csv(sample_csv)
    dept_counts = get_department_counts(df)
    expected_counts = {"HR": 1, "Engineering": 2, "Marketing": 1}
    assert dept_counts == expected_counts, f"Expected department counts {expected_counts}, got {dept_counts}."

def test_get_top_earners(sample_csv):
    # Test function 4: get_top_earners should return the top n earners.
    df = pd.read_csv(sample_csv)
    n = 2
    top_df = get_top_earners(df, n)
    # The top two salaries are 70000 and 65000 from Bob and Charlie.
    expected_names = {"Bob", "Charlie"}
    result_names = set(top_df["Name"])
    assert len(top_df) == n, f"Expected {n} rows, got {len(top_df)}."
    assert result_names == expected_names, f"Expected top earners {expected_names}, got {result_names}."
