from flask import Flask
from Config import config
from controllers import account_controller, customer_controller, transaction_controller

app = Flask(__name__)
app.config.from_object(config)

# Register blueprints
app.register_blueprint(account_controller.bp)
app.register_blueprint(customer_controller.bp)
app.register_blueprint(transaction_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)