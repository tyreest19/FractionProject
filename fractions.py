class Fraction:
	""" Object that represents a fraction"""
	
	def __init__(self, numerator, denominator, wholeNumber=0):
		"""
			Arguements:
				numerator: interger that is the numerator
				denominator: interger this is denominator
		"""
		self.numerator = numerator
		self.denominator = denominator
		self.wholeNumber = wholeNumber
	
	def __repr__(self):
		if self.numerator == self.denominator:
			return "1"
		if self.numerator % self.denominator == 0:
			return str(self.numerator//self.denominator)
		if self.wholeNumber > 0:
			return str(self.wholeNumber) + "({numerator}/{denominator})".format(
						numerator=self.numerator, denominator=self.denominator
						)	
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
		newNumerator = (self.numerator + (self.wholeNumber * self.denominator)) * y.denominator
		newNumerator += (y.numerator + (y.wholeNumber * y.denominator)) * self.denominator 
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
		if self.numerator > self.denominator:
			self.wholeNumber = self.numerator // self.denominator
			self.numerator = self.numerator % self.denominator
					
def parseInput(fraction):
	"""
		Arguement:
			fraction: Is a string of user input in the form of a fraction
		return:
			tuple containing the numerator and denominator 
	"""
	if fraction[0] == '/':
		fraction = fraction.split('/')
		numerator = int(fraction[0])
		denominator = int(fraction[1])
		return numerator, denominator, 0
	if fraction[0].isdigit():
		wholeNumber = int(fraction[0])
		fraction = fraction[2:].split('/')
		numerator = int(fraction[0])
		denominator = fraction[1]
		denominator = int(denominator[:len(denominator) - 1])
		return numerator, denominator, wholeNumber

def main():
	continueProgram = True
	while continueProgram:
		userInputFraction1 = input('Enter two fractions:\n>>')
		numerator, denominator, wholeNumber = parseInput(userInputFraction1)
		fraction1 = Fraction(numerator, denominator, wholeNumber=wholeNumber)
		userInputFraction2 = input('>>')
		numerator, denominator, wholeNumber = parseInput(userInputFraction2)
		fraction2 = Fraction(numerator, denominator, wholeNumber=wholeNumber)
		print('The sum of', fraction1, 'and', fraction2, 'is', fraction1 + fraction2)

if __name__ == '__main__':
	main()