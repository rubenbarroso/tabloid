class Paginator:
    """ """

    def __init__(self, items, page_size):
        self.page_size = page_size
        self.items = items

    def get_page(self, page_number=0):
        first_index, last_index = self._calculate_indexes(page_number)

        # if last_index > len(items), it includes all
        # items to the end of the list
        for item in self.items[first_index:last_index]:
            yield item

    def _calculate_indexes(self, page_number):
        first_index = page_number * self.page_size
        last_index = first_index + self.page_size
        return first_index, last_index

    def next_page(self, page_number=0):
        """ """
        first_index, last_index = self._calculate_indexes(page_number)
        if len(self.items) > last_index:
            return page_number + 1
        else:
            return None

    def previous_page(self, page_number=0):
        """ """
        if page_number > 0:
            return page_number - 1
        else:
            return None

    def is_empty(self):
        """ """
        return not self.items

    def is_not_empty(self):
        """ """
        return not self.is_empty()