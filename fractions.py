class Fraction:
	
	def __init__(self, numerator, denominator):
		"""
			Arguements:
				numerator: interger that is the numerator
				denominator: interger this is denominator
		"""
		self.numerator = numerator
		self.denominator = denominator
	def __repr__(self):
		if self.numerator == 1 and self.denominator == 1:
			return "1"
		return "{numerator}/{denominator}".format(
						numerator=self.numerator, denominator=self.denominator
						)				
	
	def __add__(self, y):
		""" 	
			Arguements:
				y: number being added to our fraction object
			Returns:
				New fraction object
		"""
		if y.denominator == self.denominator:
			newFraction = Fraction(self.numerator + y.numerator, 
				self.denominator)
			newFraction.simplify()
			return newFraction
		newNumerator = self.numerator * y.denominator
		newNumerator += y.numerator * self.denominator 
		newDenominator = self.denominator * y.denominator
		newFraction = Fraction(newNumerator, newDenominator)
		newFraction.simplify()
		return newFraction 
	
	def simplify(self):
		"""Simplifies Fraction"""
		reduce = True
		while reduce:	
			reduce = False
			for i in range(9, 1, -1):
				if self.numerator % i == 0 and self.denominator % i == 0:
					self.numerator //= i
					self.denominator //= i
					reduce = True
					
def parseInput(fraction):
	"""
		Arguement:
			fraction: Is a string of user input in the form of a fraction
		return:
			tuple containing the numerator and denominator 
	"""
	fraction = fraction.split('/')
	numerator = int(fraction[0])
	denominator = int(fraction[1])
	return numerator, denominator

def main():
	continueProgram = True
	while continueProgram:
		userInputFraction1 = input('Enter two fractions:\n')
		numerator, denominator = parseInput(userInputFraction1)
		fraction1 = Fraction(numerator, denominator)
		userInputFraction2 = input()
		numerator, denominator = parseInput(userInputFraction2)
		fraction2 = Fraction(numerator, denominator)
		print('The sum of', fraction1, 'and', fraction2, 'is', fraction1 + fraction2)

if __name__ == '__main__':
	main()