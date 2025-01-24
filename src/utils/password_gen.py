import array
import random


class PasswordGenerator:
    def __init__(self) -> None:
        """Initialize characters/digits/symbols for the password generation"""
        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.symbols = ["@", "#", "$", "%", "=", ":", "?", ".", "/", "|", "~", ">", "*", "(", ")", "<"]

    def gen_pass(self, password_length: int) -> str:
        """Generates random password.

        Returns:
            str: Password
        """
        # Combines all the character arrays above to form one array
        combined_list = self.digits + self.upper_case + self.lower_case + self.symbols

        # Randomly select at least one character from each character set above
        rand_digit = random.choice(self.digits)
        rand_upper = random.choice(self.upper_case)
        rand_lower = random.choice(self.lower_case)
        rand_symbol = random.choice(self.symbols)

        # Combine the character randomly selected above
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        # Fill the rest of the password length by selecting randomly from the combined list of character above.
        for _x in range(password_length):
            temp_pass = temp_pass + random.choice(combined_list)

            # Convert temporary password into array and shuffle to prevent it from having a consistent pattern
            temp_pass_list = array.array("u", temp_pass)
            random.shuffle(temp_pass_list)

        # Traverse the temporary password array and append the chars to form the password
        password = ""
        for x in temp_pass_list:
            password = password + x

        return password
