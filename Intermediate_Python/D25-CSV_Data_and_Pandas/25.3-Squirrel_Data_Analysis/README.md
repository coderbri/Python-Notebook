## Troubleshooting File Path Issues

If you encounter a **FileNotFoundError** when running the script, it’s likely due to an incorrect file path for the CSV file.

**Possible Solutions:**

1. **Check the Current Working Directory:**
   - You can use the following code snippet to check your current working directory in Python:
     ```python
     import os
     print("Current Working Directory:", os.getcwd())
     ```
   - If the CSV file is located in the same folder as the script, ensure the file is in the correct location.

2. **Use Absolute Path:**
   - If the file is located elsewhere on your system, you can use the absolute path to the CSV file:
     ```python
     data = pandas.read_csv("/full/path/to/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
     ```

3. **Use Relative Path:**
   - If the CSV is in a subdirectory, you can build the path dynamically using `os.path.join()`:
     ```python
     import os
     script_dir = os.path.dirname(os.path.abspath(__file__))
     csv_filepath = os.path.join(script_dir, "D25-CSV_Data_and_Pandas/25.3-Squirrel_Data_Analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
     data = pandas.read_csv(csv_filepath)
     ```

4. **File Missing:**
   - Ensure that the CSV file `2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv` exists in the directory you are pointing to. If it's missing, download or place the correct file in the proper folder.

If these steps do not resolve the issue, ensure the file is properly located and check for any permissions that might prevent access to the file.