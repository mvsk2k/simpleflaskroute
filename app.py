from flask import Flask, request, jsonify, render_template
import base64

app = Flask(__name__)

decoded_message = "Hi all"

@app.route('/')
def home():
    global decoded_message
    #decoded_message = "Think well and remember"
    return render_template('message.html', message=decoded_message)

@app.route('/about')
def about():
    return render_template('message.html', message=decoded_message)


if __name__ == '__main__':
    # Run the Flask app, to run in cloud run the port to be 8080
    app.run(host='0.0.0.0', port=8080)


"""
@app.route('/', methods=['POST'])
def pubsub_push_handler():
    try:
        # Extract the Pub/Sub message
        envelope = request.get_json()

        if not envelope:
            return "Bad Request: No JSON body received", 400

        # Verify the message format
        if "message" not in envelope:
            return "Bad Request: No message field in JSON", 400

        pubsub_message = envelope["message"]

        # Decode the message data (base64 encoded by Pub/Sub)
        if "data" in pubsub_message:
            message_data = pubsub_message["data"]
            decoded_message = base64.b64decode(message_data).decode("utf-8")
            #print(f"Received message: {decoded_message}")

"""
"""
        # Process any attributes
        if "attributes" in pubsub_message:
            print("Attributes:")
            for key, value in pubsub_message["attributes"].items():
                print(f"  {key}: {value}")
        """
"""
        # Process any attributes
        attributes = pubsub_message.get("attributes", {})

        # Render the HTML template with the message and attributes
        return render_template('message.html', message=decoded_message, attributes=attributes), 200

    except Exception as e:
        print(f"Error processing the message: {e}")
        return "Internal Server Error", 500

"""



