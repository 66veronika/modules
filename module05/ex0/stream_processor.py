from typing import Any, List, Tuple
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Validates if data is appropriate for this processor"""
        try:
            for i in data:
                _ = i + 1
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        total = 0
        count = 0
        for i in data:
            total += i
            count += 1
        if count == 0:
            raise ValueError("Empty numeric data")

        return (f"Processed {count} numeric values, sum={total}, "
                f"avg={total/count}")

    def format_output(self, result: str) -> str:
        """Formats the output string"""
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Validates if data is appropriate for this processor"""
        try:
            _ = data.upper()
            _ = data.split()
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        """Processes the data and returns result string"""
        if not self.validate(data):
            raise ValueError("Invalid text data")
        word_count = len(data.split())
        return (f"Processed text: {len(data)} characters, {word_count} words")

    def format_output(self, result: str) -> str:
        """Formats the output string"""
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """Validates if data is appropriate for this processor"""
        try:
            parts = data.split(":", 1)
            return len(parts) == 2
        except Exception:
            return False

    def process(self, data: Any) -> str:
        """Processes the data and returns result string"""
        if not self.validate(data):
            raise ValueError("Failed data validation")
        level, message = data.split(":", 1)
        level = level.strip().upper()
        message = message.strip()
        prefix = "[ALERT]" if level == "ERROR" else f"[{level}]"
        return f"{prefix} {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        """Formats the output string"""
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    np = NumericProcessor()
    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    res = np.process(data)
    print("Validation: Numeric data verified")
    print(np.format_output(res))

    tp = TextProcessor()
    print("\nInitializing Text Processor...")
    data = "\"Hello Nexus World\""
    print(f"Processing data: {data}")
    res = tp.process(data)
    print("Validation: Text data verified")
    print(tp.format_output(res))

    lp = LogProcessor()
    print("\nInitializing Log Processor...")
    data = "ERROR: Connection timeout"
    print(f"Processing data: \"{data}\"")
    print("Validation: Log entry verified")
    res = lp.process(data)
    print(lp.format_output(res))

    processors: List[Tuple[Any, DataProcessor]] = [
        ([2, 2, 2], NumericProcessor()),
        ("Hello, Nexus", TextProcessor()),
        ("INFO: Connection timeout", LogProcessor()),
        ("bad data", NumericProcessor()),
    ]

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    for i in range(len(processors)):
        data, processor = processors[i]
        try:
            result = processor.process(data)
            print(f"Result {i+1}: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    print("\nFoundation systems online. Nexus ready.")


if __name__ == "__main__":
    main()
