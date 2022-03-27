#!/usr/bin/env python

# import sys

keyword = input("Enter something: ").strip().lower()

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

	if keyword.isalpha():

		# fo.write('#####-----YOUR DORKS BEGIN-----#####\n')


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