import sys
import itertools as iter

banner ='''
  	 _    _               _   _ _     _
	| |  | |             | | | (_)   | |
	| |  | | ___  _ __ __| | | |_ ___| |_    __ _  ___ _ __
	| |/\| |/ _ \| '__/ _` | | | / __| __|  / _` |/ _ \ '_  |
	\  /\  / (_) | | | (_| | | | \__ \ |_  | (_| |  __/ | | |
	 \/  \/ \___/|_|  \__,_| |_|_|___/\__|  \__, |\___|_| |_|
	                                         __/ |
	                                        |___/         by Ramphy Aquino Nova
'''
usage = "\nword OPTIONS [-o] \n\n -?Lc abcdefghijklmnopqrstuvwxyz\n -?Uc ABCDEFGHIJKLMNOPQRSTUVWXYZ\n -?n  0123456789\n -?s  s!*#$?-_%&@\n\nExample: hello -?n-?s\n"

class Wordlist_gen():
	global lower_char; lower_char = 'abcdefghijklmnopqrstuvwxyz'
	global upper_char; upper_char = lower_char.upper()
	global num_char; num_char = [i for i in range(10)]
	global special_char; special_char = "!*#$?-_%&@'\/"
	global all_char; all_char = "abcdefghijklmnopqrstuvwxyz".join(upper_char) + '!*#$?-_%&'.join(str(num_char))

	global flags_dic; flags_dic = {
		'?Lc':"".join([str(i) for i in list(iter.combinations(lower_char, 1))]).replace(")", "").replace(",", "").replace("(", "").replace("'", ""),
		'?Uc':"".join([str(i) for i in list(iter.combinations(upper_char, 1))]).replace(")", "").replace(",", "").replace("(", "").replace("'", ""),
		'?n':"".join([str(i) for i in list(iter.combinations(num_char, 1))]).replace(")", "").replace(",", "").replace("(", "").replace("'", ""),
		'?s':"".join([str(i) for i in list(iter.combinations(special_char, 1))]).replace(")", "").replace(",", "").replace("(", "").replace("'", "")
	}

	def __init__(self, banner, base_word, options, optional = None):
		self.banner = banner
		self.base_word = base_word
		self.options = options
		self.optional = optional

	def function_replaces(self, word, chars):
		result = []
		for i in word:
			if i in chars: i = ""
			result.append(i)
		result = "".join(result)
		return result

	def function_option_elavoration(self):
		split_optionsBaseWord = self.options.split("-")
		join_options = "".join([flags_dic.get(key) for key in split_optionsBaseWord][1:])
		self.combination_list = []
		try:
			self.combination_list.append(list(iter.combinations(join_options, len(split_optionsBaseWord) - 1)))
		except:
			pass

	def function_join_result(self):
		try:
			if optional == None:
				print(self.banner)
				for comb in range(50000):
					print(self.base_word + self.function_replaces(str(self.combination_list[0][comb]), "(),' "))
			else:
				print(self.banner)
				print("[*]File created\n")
				file = open("".join(optional[2:]) + ".txt", 'w')
				for comb in range(50000):
					file.write(self.base_word + self.function_replaces(str(self.combination_list[0][comb]), "(),' ") + "\n")
				file.close()

		except IndexError:
			pass

try:
	optional = list(sys.argv[3] + sys.argv[4]) if len(sys.argv) > 4 else None
	wordlist_gen = Wordlist_gen(banner, sys.argv[1], sys.argv[2], optional = optional)
	wordlist_gen.function_option_elavoration()
	wordlist_gen.function_join_result()
except:
	print("{}{}".format(banner, usage))
