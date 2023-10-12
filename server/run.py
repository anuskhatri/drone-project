from app import create_app

# Create the Flask app using the factory function from your app package
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # You can set debug to False in production
