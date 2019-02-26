class generator(object):
    def __init__(self, begin, finish, step):
        if finish is None:
            finish = begin
            begin = 0
        if step is None:
            step = 1
        if finish is None:
            raise ValueError('No input data')

        assert(isinstance(begin, int))
        assert (isinstance(finish, int))
        assert (isinstance(finish, int))

        self.i = begin
        self.s = step
        self.finish = finish

        self.ok_mode = False
        self.neg_mode = False

        if begin <= finish:
            self.ok_mode = True
        elif begin >= finish:
            self.neg_mode = True



    def __iter__(self):
        while (self.ok_mode == True and self.i <= self.finish) or (self.neg_mode == True and self.i >= self.finish):
            yield self.i
            self.i += self.s

class iterator(object):
    def __init__(self, begin, finish, step):
        if finish is None:
            finish = begin
            begin = 0
        if step is None:
            step = 1
        if finish is None:
            raise ValueError('No input data')

        assert(isinstance(begin, int))
        assert (isinstance(finish, int))
        assert (isinstance(finish, int))

        self.current = begin
        self.finish = finish
        self.step = step
        self.ok_mode = False
        self.neg_mode = False

        if begin <= finish:
            self.ok_mode = True
        elif begin >= finish:
            self.neg_mode = True
    
    def __iter__(self):
        return self

    def __next__(self):
        if (self.ok_mode == True and self.current >= self.finish) or (self.neg_mode == True and self.current <= self.finish):
            raise StopIteration

        else:
            self.current += self.step
            return self.current - self.step

