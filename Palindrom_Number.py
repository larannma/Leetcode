
def isPalindrome( x: int) -> bool:
		# reverse and see if it is equal
		start = x
		if x<0:
			return False
		elif x==0:
			return True
		result = 0
		while x>0:
			target = x % 10
			result = result*10 + target

			x = x // 10
			print(f'target = {target} || result = {result} || x = {x}')
		print(f'result = {result} || start = {start}')
		return result==start 

isPalindrome(12321)