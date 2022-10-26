## Sliding window

Use case:
- Problems involving contiguous subarrays or sequences
- Can be used to reduce complexity to linear rather than polynomial
- The sliding window is either fixed in size, or it will change based on the problem

General idea:
- Initialize a left pointer denoting the window start
- Use a for loop to expand window and also to act as right pointer
- Expand window and add element or compute some sort of value with it
- Shrink window if you have reached a certain constraint or if your window size is fixed and you have grown too large