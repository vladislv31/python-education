

class Zip:

    def __init__(self, *sequences):
        self._sequences = sequences
        self._idx = 0

    def __next__(self):
        result = []
        try:
            for sequence in self._sequences:
                result.append(sequence[self._idx])
            self._idx += 1
        except IndexError:
            raise StopIteration
        return tuple(result)

    def __iter__(self):
        return self


class Chain:

    def __init__(self, *sequences):
        self._sequences = sequences
        self._seq_idx = 0
        self._item_idx = 0

    def __next__(self):
        if self._item_idx > len(self._sequences[self._seq_idx]) - 1:
            self._item_idx = 0
            self._seq_idx += 1

        if self._seq_idx > len(self._sequences) - 1:
            raise StopIteration

        result = self._sequences[self._seq_idx][self._item_idx]
        self._item_idx += 1

        return result
       
    def __iter__(self):
        return self


class Product:

    def __init__(self, *sequences):
        self.__sequences = sequences
        self.__idxs = [0 for _ in sequences]
        self.__idxs[len(self.__sequences) - 1] = -1

    def __update_indexes(self):
        prev_changed = False

        for idx, _ in enumerate(reversed(self.__sequences)):
            if idx == 0:
                if self.__idxs[len(self.__sequences) - 1 - idx] != -1:
                    prev_changed = True
                self.__idxs[len(self.__sequences) - 1 - idx] += 1
                if self.__idxs[len(self.__sequences) - 1 - idx] == len(self.__sequences[len(self.__sequences) - 1 - idx]):
                    self.__idxs[len(self.__sequences) - 1 - idx] = 0
            else:
                if prev_changed and self.__idxs[len(self.__sequences) - idx] == 0:
                    self.__idxs[len(self.__sequences) - 1 - idx] += 1
                    if self.__idxs[len(self.__sequences) - 1 - idx] == len(self.__sequences[len(self.__sequences) - 1 - idx]):
                        self.__idxs[len(self.__sequences) - 1 - idx] = 0
                else:
                    prev_changed = False

            if idx == len(self.__sequences) - 1:
                if self.__idxs[len(self.__sequences) - 1 - idx] == 0 and prev_changed:
                    raise StopIteration

    def __next__(self):
        result = []

        self.__update_indexes()
        for idx, seq in enumerate(self.__sequences):
            result.append(self.__sequences[idx][self.__idxs[idx]])

        return tuple(result)

    def __iter__(self):
        return self


if __name__ == '__main__':

    from itertools import product, chain

    print('Testing zip')
    print(list(Zip([1, 2, 3], 'abc')) == list(zip([1, 2, 3], 'abc')))
    print(list(Zip([1, 2, 3], 'abc', '12')) == list(zip([1, 2, 3], 'abc', '12')))
    print(list(Zip([1, 3], 'ab', '12')) == list(zip([1, 3], 'ab', '12')))

    print('Testing chain')
    print(list(Chain([1, 2, 3], 'abc')) == list(chain([1, 2, 3], 'abc')))
    print(list(Chain([1, 2, 3], 'abc', '12')) == list(chain([1, 2, 3], 'abc', '12')))
    print(list(Chain([1, 3], 'ab', '12')) == list(chain([1, 3], 'ab', '12')))

    print('Testing product')
    print(list(Product([1, 2], 'abcde', [1, 2, 3])) == list(product([1, 2], 'abcde', [1, 2, 3])))
    print(list(Product([1, 2], 'abe', [1, 3])) == list(product([1, 2], 'abe', [1, 3])))

