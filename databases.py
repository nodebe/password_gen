from models import Password, Session

session = Session()

#Function to store password to database
def store_password(label_password):
	label = label_password[0]
	password = label_password[1]
	existing_label_password = session.query(Password).filter_by(label=label).first()

	#insert label and password into database

	#checks to see if there is a default label Password so it can update the password instead of creating a new row and adding another label 'Password' with a new password. It helps in avoiding duplicate default
	if existing_label_password:
		current_password = existing_label_password.password
		existing_label_password.password = password
		session.commit()
		session.close()
		print("<pre>\n<span style=\"color:green\">Password for {} has been updated from {} to {}</span>\n<span style=\"color:skyblue\">Copied to the clipboard!</span>\n</pre>".format(label,current_password,password))

	else:
		new_password = Password()
		new_password.label = label
		new_password.password = password
		session.add(new_password)
		session.commit()
		session.close()

		print("<pre>\n<span style=\"color:green\">Generated password for {} is {}</span>\n<span style=\"color:skyblue\">Copied to the clipboard!</span>\n</pre>".format(label,password))

#Function to fetch from database
def fetch_password(label):
	password = session.query(Password).filter_by(label=label).first()
	if password:
		return '\n\nYour password for {} is {}'.format(password.label, password.password)
	else:
		passwords = session.query(Password).all()
		print('<pre>\n<span style=\"color:red\">No password with such label, available labels are: </span>\n</pre>\n')
		for password in passwords:
			print('-\t{}'.format(password.label))
