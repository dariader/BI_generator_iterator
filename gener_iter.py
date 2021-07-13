def generator(*args):

    if len(args) == 3:
        begin, finish, step = list(args)

    elif len(args) == 2:
        begin, finish = list(args)
        if finish >= begin:
            step = 1
        else:
            step = -1
    elif len(args) == 1:
        finish = int(args[0])
        begin = 0
        if finish >= begin:
            step = 1
        else:
            step = -1
    else:
        raise ValueError('Wrong data input error')

    assert (isinstance(begin, int))
    assert (isinstance(finish, int))
    assert (isinstance(step, int))


    current = begin
    step = step
    finish = finish

    pos_mode = False
    neg_mode = False

    if begin <= finish and step > 0:
        pos_mode = True
    elif begin >= finish:
        neg_mode = True
        if len(args) < 3:
            return []
        elif step > finish - begin:
            return []
    elif begin <= finish and step < 0:
        return []

    if len(args) == 3 and pos_mode == True and (begin == finish or step > (finish-begin)):
        return []

    while (pos_mode == True and current < finish) or (neg_mode == True and current > finish):
        yield current
        current += step


class Iterator(object):
    def __init__(self, *args):
        if len(args) == 3:
            begin, finish, step = list(args)

        elif len(args) == 2:
            begin, finish = list(args)
            if finish >= begin:
                step = 1
            else:
                step = -1
        elif len(args) == 1:
            finish = args[0]
            begin = 0
            if finish >= begin:
                step = 1
            else:
                step = -1
        else:
            raise ValueError('Wrong data input error')
        assert (isinstance(begin, int))
        assert (isinstance(finish, int))
        assert (isinstance(finish, int))


        self.current = begin
        self.finish = finish
        self.step = step
        self.pos_mode = False
        self.neg_mode = False
        self.begin_iteration = False


        if begin <= finish:
            self.pos_mode = True
        elif begin >= finish:
            self.neg_mode = True

        self.args = args

    def __iter__(self):
        return self

    def __next__(self):
        if (self.pos_mode == True and self.step < 0) or (self.neg_mode == True and self.step > 0):
            raise StopIteration
        elif self.step >= self.finish-self.current != True and len(self.args) == 3 and self.pos_mode == True and self.begin_iteration == False:
            raise StopIteration

        else:
            self.begin_iteration = True
            while self.current < self.finish:
                self.current = self.current + self.step
                return self.current - self.step
            raise StopIteration
