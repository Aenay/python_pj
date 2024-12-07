class Thing:
    def __init__(self, name, type_, color, weight, age):
        self.name = name
        self.type = type_
        self.color = color
        self.weight = self.validate_float(weight, "Weight")  # Validate weight input
        self.age = self.validate_int(age, "Age")  # Validate age input

    def validate_float(self, value, field_name):
        """Helper function to validate float values (e.g., weight)"""
        try:
            return float(value)  # Try converting value to float
        except ValueError:
            print(f"Invalid {field_name}. Please enter a valid number for {field_name}.")
            return 0.0  # Default value if conversion fails

    def validate_int(self, value, field_name):
        """Helper function to validate integer values (e.g., age)"""
        try:
            return int(value)  # Try converting value to int
        except ValueError:
            print(f"Invalid {field_name}. Please enter a valid integer for {field_name}.")
            return 0  # Default value if conversion fails

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "color": self.color,
            "weight": self.weight,
            "age": self.age
        }

    def update(self, type_=None, color=None, weight=None, age=None):
        if type_:
            self.type = type_
        if color:
            self.color = color
        if weight:
            self.weight = self.validate_float(weight, "Weight")  # Validate weight when updating
        if age:
            self.age = self.validate_int(age, "Age")  # Validate age when updating

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Color: {self.color}, Weight: {self.weight}, Age: {self.age}"

