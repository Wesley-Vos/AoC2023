from __future__ import annotations
import regex as re


class Trebuchet:
    def calibrate(self, input_file) -> int:
        return self.Calibrator(filename=input_file).run()

    def convert_and_calibrate(self, input_file):
        return self.Calibrator(filename=input_file, convert_digits=True).run()

    class Calibrator:
        raw_document: list = None
        document: list = None

        def __init__(self, filename: str, convert_digits=False):
            self._read_document(filename)
            self._fix_document(convert_digits)

        def _read_document(self, filename: str) -> None:
            with open(filename) as input_file:
                self.raw_document = input_file.read().splitlines()

        def _fix_document(self, convert_digits) -> None:
            re_pattern = "1|2|3|4|5|6|7|8|9" + ('|one|two|three|four|five|six|seven|eight|nine' if convert_digits else "")
            mapping = {n: (i % 9) + 1 for i, n in enumerate(re_pattern.split('|'))}

            def _execute(line, pattern) -> int:
                matches = re.findall(pattern, line, overlapped=True)
                return (mapping.get(matches[0]) * 10) + mapping.get(matches[-1])

            self.document = [_execute(line, re_pattern) for line in self.raw_document]

        def run(self) -> int:
            return sum(self.document)
