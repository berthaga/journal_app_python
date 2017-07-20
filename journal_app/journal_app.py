import journal
def main():
	print_header()
	run_event_loop()
	# list_entries(data)
	# add_entry(data)

def print_header():
	print'--------------------------------------'
	print'--------- JOURNAL APP'
	print'--------------------------------------'

def run_event_loop():
	print 'What do you want to do with your Journal? '
	
	cmd = 'Empty'
	journal_name='default'
	journal_data=journal.load(journal_name)

	while cmd!='x' and cmd:
		cmd = raw_input('[L]ist Entries, [A]dd an entry, E[x]it: ')
		cmd= cmd.lower().strip()

		if cmd=='l':
			list_entries(journal_data)

		elif cmd=='a':
			add_entry(journal_data)

		# # my code

		# elif cmd=='d':
		# 	del_entry(journal_data)

		# # end

		elif cmd!='x' and cmd:
			print "Sorry, I don't understand'{}'".format(cmd)

	print'Done. Goodbye'
	journal.save(journal_name,journal_data)

def list_entries(data):
	print 'Your Journal Entries:  '
	entries=reversed(data)
	for index, entry in enumerate(entries):
		print '*[{}] {}'.format(index+1,entry)

def add_entry(data):
	text=raw_input('Type your entry, <enter> to exit: ')
	journal.add_entry(text,data)

# my code

# def del_entry(data):
#  	data=input('Type the number of the entry you want to delete: ')
#  	journal.delete_entry(data)

# end

	

main()