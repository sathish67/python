PYTHON BASICS
│
├── 1. Variables & Data Types
├── 2. Operators
├── 3. if / elif / else
├── 4. for / while loops
├── 5. Functions
├── 6. Lambda Functions
├── 7. List / Tuple / Set / Dictionary
├── 8. Comprehensions
├── 9. Exception Handling
├── 10. Modules
├── 11. Packages
└── 12. File Handling


DataTypes are 

int, float, complex, bool
str, list, tuple, set, dict, None


tuple:

Ordered: Elements maintain a defined order that will not change.
Immutable: You cannot append, remove, or alter elements after creation.
Heterogeneous: A single tuple can hold elements of different data types (e.g., strings, integers, lists).Allows Duplicates: The same value can appear multiple times.
Hashable: If all elements inside a tuple are immutable, the tuple itself can be used as a dictionary key or a set element (which lists cannot do).


Set:

No Duplicates: If you add a duplicate item, Python will automatically ignore it.
Unordered & Unindexed: Elements do not have a fixed order. You cannot access them using an index like fruits[0].
Heterogeneous: A single set can store a mix of different data types (e.g., integers, strings, booleans).


Dict

Ordered: Starting with Python 3.7, dictionaries preserve insertion order. When you loop through a dictionary, items appear in the exact order they were added.
Mutable: You can add, change, or remove items after the dictionary is created.
Unique Keys: Duplicate keys are not allowed. If you assign a value to an existing key, it simply overwrites the old value.
Data Type Flexibility: Keys must be of an immutable (hashable) data type, such as strings, numbers, or tuples. You cannot use a list or another dictionary as a key.Values can be of any data type (strings, integers, lists, or even other nested dictionaries) and can repeat.
Highly Efficient: Because they are implemented using hash tables, looking up a value by its key is extremely fast, regardless of how large the dictionary is.


/   → division
//  → floor division
%   → remainder
**  → power

According to official Python style guidelines (PEP 8), you should avoid assigning lambda expressions directly to identifiers (e.g., square = lambda x: x**2). If a function requires a name, it is always cleaner and better for debugging to define it using def. Use lambdas purely for quick, throwaway, single-line logic.