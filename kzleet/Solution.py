class Solution(object):
    def __init__(self, author, date):
        self.author = author
        self.date = date

    def __str__(self):
        return f'LeetCode Solution by {self.author} on {self.date}'

    def main(self, *args):
        '''
        Main method of the solution class.
        Override this method in subclasses to implement the solution logic.
        Define the solution solution(...): -> and set main = solution
        '''

        raise NotImplementedError('Subclasses should implement this method; set it equal to the solution.')