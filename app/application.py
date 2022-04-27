from tw33t import app
import logging
logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

#Development
#application.run(host='0.0.0.0', threaded=True, port=5000, debug=True)

#Deployment to production or staging
if __name__ == "__main__":
	app.run(debug=True, threaded=False, host='0.0.0.0')
