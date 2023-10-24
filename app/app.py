from flask import Flask, request, redirect
import MySQLdb
import config

app = Flask(__name__)

@app.route('/collect')
def collect_data():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    location = 'DummyLocation'  # Replace with actual logic or API call for location

    # Connect to MySQL
    db = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASS, db=config.DB_NAME)
    cur = db.cursor()
    
    # Insert data
    cur.execute("INSERT INTO user_data (ip_address, user_agent, location) VALUES (%s, %s, %s)", 
                (ip_address, user_agent, location))
    db.commit()
    
    cur.close()
    db.close()
    
    # Redirect to legitimate website
    return redirect('https://google.com')

if __name__ == '__main__':
    app.run()
