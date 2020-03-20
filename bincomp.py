import os


class BinaryComparator:

    def __init__(self, file1, file2):
        self._buffer_size = 512

        self.message = None
        self.offset = None
        self.diff_list = []
        self.failed_percent = 0.0

        self.file1 = file1
        self.file2 = file2

    def compare(self):
        self.message = None
        self.offset_differs = None
        offset = 0
        offset_diff = 0
        first = False

        if not os.path.isfile(self.file1) or not os.path.isfile(self.file2):
            self.message = "not found"
            return False

        # if os.path.getsize(self.file1) != os.path.getsize(self.file2):
        #     self.message = "size"
        #     return False

        result = True
        f1 = open(self.file1, 'rb')
        f2 = open(self.file2, 'rb')

        all = 0
        failed = 0
        loop = True
        while loop:
            buffer1 = f1.read(self._buffer_size)
            buffer2 = f2.read(self._buffer_size)
            if len(buffer1) == 0 or len(buffer2) == 0:
                loop = False

            for e in range(len(list(zip(buffer1, buffer2)))):
                if buffer1[e] != buffer2[e]:
                    if not first:
                        first = True
                    result = False
                    failed = failed + 1
                    self.diff_list.append((hex(offset), hex(buffer1[e]), hex(buffer2[e])))

                all = all + 1
                offset += 1
                if not first:
                    offset_diff += 1
        f1.close()
        f2.close()

        self.failed_percent = failed / all

        if not result:
            self.message = 'content'
            self.offset = hex(offset_diff)
        else:
            self.message = 'identical'

        return result

