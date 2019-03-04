from flask import Flask
from fakebook_pac import app

if __name__ == "__main__":
	app.run(debug=True)


"""in order to run the sever on power shell:
$env:FLASK_APP="blog.py"
flask run"""