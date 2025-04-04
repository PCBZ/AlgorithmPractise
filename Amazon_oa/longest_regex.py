
class Solution:
    def findLongestRegex(self, x: str, y: str, z: str) -> str:
        def matchRegex(s: str, regex: str) -> bool:
            s_idx = r_idx = 0
            while s_idx < len(s) and r_idx < len(regex):
                if r_idx == '[':
                    end_r_idx = regex.find(']')
                    if end_r_idx == -1:
                        return False
                    branket = regex[r_idx+1:end_r_idx]
                    if s[s_idx] not in branket:
                        return False
                    r_idx = end_r_idx + 1
                    s_idx += 1
                else:
                    if s[s_idx] != regex[r_idx]:
                        return False
                    s_idx += 1
                    r_idx += 1
            return s_idx == len(s) and r_idx == len(regex)
        

        n = len(x)
        alphabeta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        regex = []
        for i in range(n):
            options = []
            if x[i] == y[i] and x[i] != z[i]:
                options.append(x[i])
            
            if x[i] != y[i] and x[i] != z[i] and y[i] != z[i]:
                comb = ''.join(sorted([x[i], y[i]]))
                options.append('[' + comb + ']')

            chars = "".join(sorted([ch for ch in alphabeta if ch != z[i]]))
            if x[i] in chars and y[i] in chars:
                options.append('[' + chars + "]")
            
            if not options:
                return -1
            
            options.sort(key = lambda x: (-len(x), x))
            regex.append(options[0])
        
        res = "".join(regex)

        if matchRegex(x, res) and matchRegex(y, res) and not matchRegex(z, res):
            return res
        return -1

    def findLongestRegex2(self, x, y, z):
        n = len(x)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # Helper function to check if a string matches a regex
        def string_matches_regex(s, regex):
            s_idx = 0  # String index
            r_idx = 0  # Regex index
            
            while s_idx < len(s) and r_idx < len(regex):
                if regex[r_idx] == '[':
                    # Find the closing bracket
                    end_idx = regex.find(']', r_idx)
                    if end_idx == -1:
                        return False  # Unbalanced brackets
                    
                    # Get the character class
                    char_class = regex[r_idx+1:end_idx]
                    
                    # Check if current string character is in the class
                    if s[s_idx] not in char_class:
                        return False
                    
                    # Move past the character class in regex and the character in string
                    r_idx = end_idx + 1
                    s_idx += 1
                else:
                    # Direct character match
                    if regex[r_idx] != s[s_idx]:
                        return False
                    r_idx += 1
                    s_idx += 1
            
            # Both string and regex should be fully consumed
            return s_idx == len(s) and r_idx == len(regex)
        
        # For each position, we'll choose the option that contributes to the longest regex
        regex = []
        
        for i in range(n):
            position_options = []
            
            # Option a: Direct character (length 1)
            if x[i] == y[i] and x[i] != z[i]:
                position_options.append((x[i], 1))
            
            # Option b: Character class with just x[i] and y[i]
            if x[i] != y[i] and z[i] != x[i] and z[i] != y[i]:
                char_class = "".join(sorted([x[i], y[i]]))
                position_options.append(("[" + char_class + "]", len("[" + char_class + "]")))
            
            # Option c: Character class with all letters except z[i]
            excluded = z[i]
            char_class = "".join(sorted([c for c in alphabet if c != excluded]))
            if x[i] in char_class and y[i] in char_class:
                position_options.append(("[" + char_class + "]", len("[" + char_class + "]")))
            
            # If no options, we can't build a valid regex
            if not position_options:
                return "-1"
            
            # Sort options by length (descending) and then lexicographically (ascending)
            position_options.sort(key=lambda opt: (-opt[1], opt[0]))
            regex.append(position_options[0][0])
        
        # Verify the regex matches x and y but not z
        result = "".join(regex)
        if string_matches_regex(x, result) and string_matches_regex(y, result) and not string_matches_regex(z, result):
            return result
        else:
            return "-1"


if __name__ == "__main__":
    x = "AB"
    y = "BD"
    z = "CD"
    
    print(Solution().findLongestRegex2(x, y, z))

    t = "[ABDEFGHIJKLMNOPQRSTUVWXYZ)[ABCDEFGHIJKLMNOPQRSTUVWXYZ]"
