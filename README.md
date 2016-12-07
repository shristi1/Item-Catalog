## Synopsis
An application that provides a list of items within a variety of categories including a user registration and authentication system.


## How Do I Use This?
To run this program locally on your computer:
	1. Make sure you have VirtualBox and Vagrant installed on your computer

	2. In your terminal navigate to the vagrant folder in which the files for the catalog program are written.

	3. Then, run vagrant up and vagrant ssh:
		1. vagrant up
		2. vagrant ssh

	4. CD into the catalog folder inside the vagrant directory
		1. cd /vagrant/catalog/

	5. Initialize the database:
		1. python database_setup.py

	6. Then, populate the database with a few categories and items:
		1. python additems.py

	7. Run the application:
		1. python application.py 

	8. Navigate to "localhost:5000/" to see the website running locally on your computer