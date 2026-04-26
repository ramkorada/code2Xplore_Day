# Multi-Level Data Replication & Integrity Analyzer

## Overview

This project simulates how data is replicated across systems and analyzes issues that arise due to improper copying techniques. It demonstrates the differences between assignment, shallow copy, and deep copy in Python, and shows how unintended data modification (data leakage) can occur in nested data structures.

## Problem Statement

A cloud system replicates user data across servers. Due to incorrect copying methods, data inconsistency may occur. This program creates a nested data structure, performs different types of copying, applies modifications, and analyzes data integrity.

## Features

* Nested data structure using lists and dictionaries
* Implementation of assignment, shallow copy, and deep copy
* Multi-level data modification
* Detection of data leakage
* Integrity analysis using sets and comparisons
* Clear before and after comparison of data

## Technologies Used

* Python
* Built-in `copy` module

## Data Structure

```python
users = [
    {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
    {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
]
```

## Functions Used

* `generate_data()` – creates initial dataset
* `replicate_data()` – performs assignment, shallow copy, and deep copy
* `modify_data()` – applies changes to copied data
* `check_integrity()` – analyzes data consistency and corruption

## Personalization Rule

Last digit of Register Number: 2
Since it is even, the program applies the "add new file" logic during modification.

## Logic and Approach

1. Create a nested data structure.
2. Generate three versions: assignment, shallow copy, and deep copy.
3. Modify copied data by adding a file, updating usage, and removing one file.
4. Compare results to detect unintended changes.
5. Use sets to find overlapping data.
6. Generate an integrity report.

## Definition of Data Corruption

Data corruption is defined as any unexpected change in the original data when only the copied data is modified.

## Sample Output

```
BEFORE
[{'id': 1, 'data': {'files': ['a.txt', 'b.txt'], 'usage': 500}}, {'id': 2, 'data': {'files': ['c.txt'], 'usage': 300}}]

AFTER
Original: [{'id': 1, 'data': {'files': ['b.txt', 'new_file.txt'], 'usage': 600}}, {'id': 2, 'data': {'files': ['new_file.txt'], 'usage': 400}}]
Shallow: [{'id': 1, 'data': {'files': ['b.txt', 'new_file.txt'], 'usage': 600}}, {'id': 2, 'data': {'files': ['new_file.txt'], 'usage': 400}}]
Deep: [{'id': 1, 'data': {'files': ['b.txt', 'new_file.txt'], 'usage': 600}}, {'id': 2, 'data': {'files': ['new_file.txt'], 'usage': 400}}]

REPORT
(2, 0, 2)
```

## Key Concepts Demonstrated

* Difference between assignment, shallow copy, and deep copy
* Impact of modifying nested structures
* Data leakage due to shared references
* Safe data handling using deep copy
* Use of sets for overlap detection

## Learning Outcome

This project helps in understanding how different copying methods behave in Python and how improper handling of nested data can lead to data inconsistency. It also demonstrates practical ways to detect and analyze such issues.

## Conclusion

Proper data replication is critical in real-world systems. This project highlights how small mistakes in copying data can lead to serious integrity issues and shows how to prevent them using correct techniques.
