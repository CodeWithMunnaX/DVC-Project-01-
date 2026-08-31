import pandas as pd
import numpy as np

# Reproducible random data
np.random.seed(42)

# Number of students
n = 10

# Generate data
data = {
    "student_id": np.arange(1, n + 1),
    "name": [f"Student_{i}" for i in range(1, n + 1)],
    "age": np.random.randint(18, 25, n),
    "marks": np.random.randint(40, 100, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("data/student.csv", index=False)

print("Student dataset created successfully!")
print(df)