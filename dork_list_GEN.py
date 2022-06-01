#!/usr/bin/env python

import sys

isInstagram = True

def createQueries(keyword, *args, **kwargs):
	# keyword = input("Enter something: ").strip().lower()

	with open(f"dork_list.txt", "w+", encoding="utf-8") as fo:
		# lines = fo.readlines()
		# line_offset = []
		# offset = 0

		# for i, line in enumerate(lines):
		# 	line_offset.append(offset)
		# 	offset += len(line)
		# 	print(i, line)
		# 	if line.endswith('\n'):
		# 		considered good to be used in production code
		# 		sys.exit("End of File")
		# 		fo.write('\n')
		# 		break
		# fo.seek(0)
		# fo.seek(line_offset[n])	# go to line number n

		flag = True
		for i in range(len(keyword)):
			if not (keyword[i].isalpha() or keyword[i].isspace()):
				flag = False
				break

		if flag:
			# fo.write('#####-----YOUR DORKS BEGIN-----#####\n')

			if isInstagram:
				fo.write('{} inurl:instagram.com -tags -channel\n'.format(keyword))
			else:
				fo.write('{} inurl:"ac.in" intext:"@gmail.com" or "+91" filetype:xlsx\n'.format(keyword))

				fo.write('{} filetype:env\n'.format(keyword))

				fo.write('intext:"{}" filetype:log\n'.format(keyword))

				fo.write('intext:"{}" filetype:xslx\n'.format(keyword))

				fo.write('intext:"{}"\n'.format(keyword))

				# fo.write('intext:"{}" filetype:pdf\n'.format(keyword))	# abnormal output!!!

				fo.write('inurl:{}\n'.format(keyword))

				fo.write('{} inurl:/proc/self/cwd\n'.format(keyword))

				fo.write('intitle:{}\n'.format(keyword))

				fo.write('intitle:{} inurl:ftp\n'.format(keyword))

				fo.write('inanchor:{}\n'.format(keyword))


			# fo.write('#####-----YOUR DORKS END-----#####')

		else:
			print("Invalid Input")

if __name__ == "__main__":
    createQueries(sys.argv[1])