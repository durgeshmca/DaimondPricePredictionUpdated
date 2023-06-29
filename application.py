from flask import Flask,render_template,request,jsonify
from src.pipelines.prediction_pipeline import PredictPipeline,CustomData
import sys
from src.exception import CustomException

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict_datapoint',methods=['GET','POST'])
def predict_datapoint():
    try :
        if request.method == 'GET' :
            return render_template('form.html')
        else :
            formData = {
                'carat'   : float(request.form.get('carat')),
                'cut'     : request.form.get('cut'),
                'color'   : request.form.get('color'),
                'clarity' : request.form.get('clarity'),
                'depth'   : float(request.form.get('depth')),
                'table'   : float(request.form.get('table')),
                'x'       : float(request.form.get('x')),
                'y'       : float(request.form.get('y')),
                'z'       : request.form.get('z')
            }
            data = CustomData(
                carat   = formData['carat'],
                cut     = formData['cut'],
                color   = formData['color'],
                clarity = formData['clarity'],
                depth   = formData['depth'],
                table   = formData['table'],
                x       = formData['x'],
                y       = formData['y'],
                z       = formData['z']

            )
            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            predicted= predict_pipeline.predict(final_new_data)
            predicted_value  =  round(predicted[0],2)

            return render_template('form.html',final_result = predicted_value)
    
    except Exception as e:
        # ce = CustomException(e,sys)
        return render_template('form.html',final_result = e)
        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,   debug=True)
