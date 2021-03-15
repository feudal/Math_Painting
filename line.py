class Dot:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y - 1:self.y, self.x - 1:self.x] = self.color

class Line:

    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def duplicate_missing_dots(self, sl, ll):
        short_list = sl.copy()
        long_list = ll.copy()
        list_of_list = []
        multiplication = int((len(long_list) / len(short_list)))

        for i in range(multiplication):
            list_of_list.append(short_list)

        # zip all the list in one list
        list_of_list = list(zip(*list_of_list))

        # join all tuples in one list with list comprehension
        new_list_of_points = [item for t in list_of_list for item in t]

        points_ramin = len(long_list) - len(short_list) * multiplication
        # if we don't have points to assign to list we exit
        if points_ramin == 0:
            # exit
            return new_list_of_points

        # we generate some values for points that remain and assign to list points_ramin_list
        # and after to new_list_of_points
        # [1,2,3,4,5,6,7,8,9]
        # [1,3,6,8]
        # [1,1,2,3,3,4,5,6,6,7,8,8,9]
        points_ramin_list = []
        step_nr_generated = int(len(short_list) / points_ramin + 0.5)
        for i in range(short_list[0], short_list[-1] + 1, step_nr_generated):
            points_ramin_list.append(i)

        # we assign list points_ramin_list to new_list_of_points
        new_list_of_points = new_list_of_points + points_ramin_list
        new_list_of_points.sort()

        return new_list_of_points

    def draw(self, canvas):

        nr_of_dots_x = abs(self.x1 - self.x2)
        nr_of_dots_y = abs(self.y1 - self.y2)

        # create to list of dots one for x other for y
        # in the end this will be the coordinates of the line
        list_dots_x = []
        list_dots_y = []
        for i in range(self.x1, self.x2 + 1):
            list_dots_x.append(i)

        for i in range(self.y1, self.y2 + 1):
            list_dots_y.append(i)

        if self.y2 < self.y1:
            for i in range(self.y1, self.y2, -1):
                list_dots_y.append(i)

        # with method duplicate_missing_dots we give new value for one list of coordinates (x or y)
        # the length list of coordinates for x must be equal with list of coordinates y
        if nr_of_dots_x > nr_of_dots_y:
            list_dots_y = self.duplicate_missing_dots(list_dots_y, list_dots_x)
        else:
            list_dots_x = self.duplicate_missing_dots(list_dots_x, list_dots_y)

        if self.y2 < self.y1 and (list_dots_y[0] < list_dots_y[-1]):
            list_dots_y.reverse()
        # join coordinates x and y of the line in a list
        list_dots_x_y = list(zip(list_dots_x, list_dots_y))

        for i in range(len(list_dots_x_y)):
            canvas.data[list_dots_x_y[i][1] - 1:list_dots_x_y[i][1],
            list_dots_x_y[i][0] - 1:list_dots_x_y[i][0]] = self.color

