keyword = input("Enter something: ")

with open(f"dork_list.txt", "a", encoding="utf-8") as fo:
	fo.write('#####-----YOUR DORKSBEGIN-----#####\n')


	fo.write('{} inurl:"ac.in" intext:"@gmail.com" or "+91" filetype:xlsx\n'.format(keyword))

	fo.write('intext:"{}"\n'.format(keyword))

	fo.write('intext:"{}" filetype:log\n'.format(keyword))

	fo.write('intext:"{}" filetype:xslx\n'.format(keyword))

	# fo.write('intext:"{}" filetype:pdf\n'.format(keyword))

	fo.write('inurl:{}\n'.format(keyword))

	fo.write('{} inurl:/proc/self/cwd\n'.format(keyword))

	fo.write('intitle:{}\n'.format(keyword))

	fo.write('intitle:{} inurl:ftp\n'.format(keyword))

	fo.write('inanchor:{}\n'.format(keyword))

	fo.write('{} filetype:env\n'.format(keyword))


	fo.write('#####-----YOUR DORKS END-----#####')