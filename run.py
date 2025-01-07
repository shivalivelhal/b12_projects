from app import create_app    #this create_app come from __init__.py which is in app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)