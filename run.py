from crowd import create_app, db
#from crowd.generatedata import generate_users # for generate test data

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        #generate_users(app) # for generate test data
        app.run(debug=True, port=5000)