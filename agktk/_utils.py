# noinspection PyShadowingBuiltins
def iter_id(id: int = 100001):
    """An infinite, unique id generator."""
    while True:
        yield id
        id += 1


# class IndexedProperty(object):
#     def __init__(self, getter: callable, setter: callable):
#         self._getter = getter
#         self._setter = setter
#
#     def __getitem__(self, index):
#         return self._getter(index)
#
#     def __setitem__(self, index, value):
#         self._setter(index, value)
    # self._byte = IndexedProperty(lambda index: _get_memblock_byte(self.__id, index),
    #                              lambda index, value: _set_memblock_byte(self.__id, index, value))
    #
    # @property
    # def byte(self) -> IndexedProperty:
    #     return self._byte
    #
