
class MonthBlock():

    def __init__(self, month, items):

        self.month = month,
        self.block_colors = {

            0: 'rgb(223, 219, 219)',
            1: 'rgb(225, 238, 255)',
            5: 'rgb(182, 213, 255)',
            10: 'rgb(117, 174, 255)',
            20: 'rgb(40, 129, 255)'

        }
        self.color = self.get_color(items)

    def get_color(self, month_items):

        limit_items = list(self.block_colors.keys())

        for index in range(5):

            if month_items == limit_items[index]:

                return self.block_colors[limit_items[index]]

            elif month_items < limit_items[index]:

                return self.block_colors[limit_items[index-1]]

            elif month_items > 20:

                return self.block_colors[20]