class slip:
    def get_String(self):
        self.str=input("Enter a string :")
    def print_string(self):
        print("Uppercase:",self.str.upper())
        print("Reversed:",' '.join(reversed(self.str.split())).lower())

s=slip()
s.get_String()
s.print_string()
