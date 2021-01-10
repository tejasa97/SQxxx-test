import operator


class Heap:
    def __init__(self):
        self.lst = []
        self.is_bigger_than = operator.lt

    def add(self, x):
        self.lst.append(x)
        idx_node = len(self.lst) - 1
        self._siftup(idx_node)

    @property
    def length(self):

        return len(self.lst)

    def pop(self):
        if len(self.lst) == 0:
            return None
        else:
            lst = self.lst
            lst[0], lst[-1] = lst[-1], lst[0]  # switch first with last element
            res = lst.pop()  # pop last element
            self._siftdown(0)
            return res

    def _siftup(self, inode):
        lst = self.lst
        iparent = self._get_parent(inode)
        if iparent >= 0 and self.is_bigger_than(lst[inode], lst[iparent]):
            lst[inode], lst[iparent] = lst[iparent], lst[inode]
            self._siftup(iparent)

    def _siftdown(self, inode):
        lst = self.lst
        ichildren = self._get_children(inode)
        for ichild in ichildren:  # do I need to sift down
            if ichild < len(lst) and self.is_bigger_than(lst[ichild], lst[inode]):
                lst[ichild], lst[inode] = lst[inode], lst[ichild]
                self._siftdown(ichild)

    def _get_parent(self, idx_child):
        idx_parent = int((idx_child - 1) / 2)  # zero-based array
        return idx_parent

    def _get_children(self, idx_parent):
        idx_children = 2 * idx_parent + 1, 2 * idx_parent + 2
        return idx_children
