#  Date: 5/4/2021, 2nd Year B.Tech CSE


class PaginationHelper:
    def __init__(self, coll, items_per_page):
        self.__pages = coll
        self.__items_per_page = items_per_page

    def item_count(self):
        return len(self.__pages)

    def page_count(self):
        b = len(self.__pages)
        l = self.__items_per_page

        isNotdvisible = b // l
        extra = 1 if isNotdvisible else 0
        return (b // l) + extra

    def page_item_count(self, page_index):
        pages = self.page_count()
        # print(pages)
        if page_index < pages:
            if page_index == pages - 1:
                return len(self.__pages) % self.__items_per_page
            else:
                return self.__items_per_page
        return -1

    def page_index(self, item_index):
        if item_index >= len(self.__pages) or item_index < 0:
            return -1
        return item_index // self.__items_per_page


p1 = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
# print(p1.page_item_count(1))
helper = p1
print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(0))
print(helper.page_item_count(1))
print(helper.page_item_count(2))
print()
# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))
print(helper.page_index(-10))
