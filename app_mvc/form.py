# from django import forms

class Cofee:
    sum = {'total':0, 'milk':0}
    def milk01(self, y, x):
        self.sum['total'] += y
        self.sum['milk'] += x
        return(self.sum['total'], self.sum['milk'])
