def find_longest_regex(x, y, z):
    n = len(x)
    
    # Initialize variables
    regex = []
    excluded_z = False
    
    # Check if it's possible to create a regex that doesn't match z
    for i in range(n):
        if x[i] != z[i] or y[i] != z[i]:
            excluded_z = True
            break
    
    if not excluded_z:
        return "-1"
    
    # Reset flag for building the regex
    excluded_z = False
    
    for i in range(n):
        # For each position, determine what characters are needed
        chars_needed = {x[i], y[i]}
        
        # Check if we can exclude z[i] at this position
        can_exclude_z_here = z[i] not in chars_needed
        
        # If we haven't excluded z yet and we can do it here
        if not excluded_z and can_exclude_z_here:
            # Create a character class with all uppercase letters except z[i]
            all_chars_except_z = []
            for c in range(ord('A'), ord('Z')+1):
                char = chr(c)
                if char != z[i]:
                    all_chars_except_z.append(char)
            
            regex.append("[" + "".join(all_chars_except_z) + "]")
            excluded_z = True
        else:
            # We've already excluded z or can't exclude it at this position
            # If x[i] and y[i] are the same, use a single character (lexicographically smaller)
            if len(chars_needed) == 1:
                regex.append(next(iter(chars_needed)))
            else:
                # Use a character class with all uppercase letters
                all_chars = [chr(c) for c in range(ord('A'), ord('Z')+1)]
                regex.append("[" + "".join(all_chars) + "]")
    
    return "".join(regex)

# Example
x = "AE"
y = "BE"
z = "CD"
result = find_longest_regex(x, y, z)
print(result)  # Should output "[ABDEFGHIJKLMNOPQRSTUVWXYZ][ABCDEFGHIJKLMNOPQRSTUVWXYZ]"