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
            re_pattern = "1|2|3|4|5|6|7|8|9"
            replace_mapping = {
                "one": '1',
                "two": '2',
                "three": '3',
                "four": '4',
                "five": '5',
                "six": '6',
                "seven": '7',
                "eight": '8',
                "nine": '9'
            }

            def _execute(line, pattern) -> int:
                _replace = lambda x: x if x.isdigit() else replace_mapping[x]
                matches = re.findall(pattern, line, overlapped=True)
                return int(_replace(matches[0]) + _replace(matches[-1]))

            re_pattern = re_pattern + ('|'.join(replace_mapping.keys()) if convert_digits else "")
            self.document = [_execute(line, re_pattern) for line in self.raw_document]

        def run(self) -> int:
            return sum(self.document)
