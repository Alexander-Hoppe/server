from flask import Flask, request
import model

service = Flask(__name__)

@service.route('/polarizingornot')
def evaluate_model():
    # if key doesn't exist, returns None
    socialmedia = request.args.get('socialmedia')

    # if key doesn't exist, returns a 400, bad request error
    sourcecontent = request.args['sourcecontent']

    content_rating = model.calc_polarizing_probability(socialmedia, sourcecontent)

    return str(content_rating)
#          '''    The social media site value is: {}
#              The content value is: {}
#              '''.format(socialmedia, sourcecontent)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    service.run(debug=True, host='192.168.178.45', port=5000)

