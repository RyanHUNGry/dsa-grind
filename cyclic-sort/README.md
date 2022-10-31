## Cyclic sort

Use case:
- Problems involving arrays with numbers in a given range
    - [1, n] or [0, n] or something similar
    - First missing positive number
    - Duplicates
- Can be used to sort or look for missing values in linear time and constant space

General idea:
- Let the index of the array denote the value of the number; the range should hint at what number corresponds to which index
    - For instance, if your range is [1, n], then your 0th index should hold 1
- Place numbers into their correct index locations
- If the problems allows duplicate (non-unique) numbers, make sure to check for infinite cycles
