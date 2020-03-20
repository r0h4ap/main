SPAN_STYLE = "<span style=\"color:red;\">"
SPAN_END = "</span>"


class TextComparator:

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

        self.text1_result = ''
        self.text2_result = ''

    def compare(self):
        with open(self.file1, 'r') as file:
            content1 = file.read()

        with open(self.file2, 'r') as file:
            content2 = file.read()

        result1 = ''
        result2 = ''

        opened = False
        prev_compare = True
        min_len = min(len(content1), len(content2))

        for i in range(min_len):
            prev = ''
            if prev_compare and content1[i] != content2[i]:
                prev_compare = False
                prev = SPAN_STYLE
                opened = True
            elif not prev_compare and content1[i] == content2[i]:
                prev_compare = True
                if opened:
                    prev = SPAN_END
                    opened = False

            result1 = result1 + prev + ("<br>" if content1[i] == '\n' else content1[i])
            result2 = result2 + prev + ("<br>" if content2[i] == '\n' else content2[i])

        if not prev_compare:
            result1 = result1 + SPAN_END
            result2 = result2 + SPAN_END

        if min_len < len(content1):
            result1 = result1 + SPAN_STYLE + content1[min_len:].replace('\n', "<br>") + SPAN_END
        elif min_len < len(content2):
            result2 = result2 + SPAN_STYLE + content2[min_len:].replace('\n', "<br>") + SPAN_END

        return result1, result2

