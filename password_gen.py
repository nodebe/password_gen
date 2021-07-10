import fire, random, clipboard
from databases import store_password, fetch_password

#creating parameters lists
upcase_list=','.join("ABCDEFGHIJKLMNOPQRSTUVWXYZ").split(',')
lowcase_list=','.join("abcdefghijklmnopqrstuvwxyz").split(',')

numbers_list=','.join("0123456789").split(',')

symbols_list=','.join("@#_&+()/*;!?~$%").split(',')
	

def intro(label='Password', length=8, nosymbols=False, nonumbers=False, fetch=''):
	global upcase_list, lowcase_list, numbers_list, symbols_list

	#if user performs a fetch operation
	if fetch:
		return fetch_password(fetch)

	#variable where generated password will store
	generated_password  = ''

	#checking user input for non-required parameters and making their lists empty
	if nosymbols:
		symbols_list = []
	if nonumbers:
		numbers_list = []
		
	#Joining all parameters list together
	required_parameters = symbols_list+numbers_list+upcase_list+lowcase_list

	#loop checking if --length and label is given by user in input
	for i in range(0, length):
		generated_password += random.choice(required_parameters)

	#copy generated password to clipboard
	clipboard.copy(generated_password)

	return store_password([label, generated_password])

if __name__ == '__main__':
	fire.Fire(intro)