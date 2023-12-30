from flask import Flask, jsonify
from celery_app import celery
from celery.result import AsyncResult
from tasks.task1 import task1


app = Flask(__name__)


@app.route('/simple')
def simple():
    res = 'cool2'
    return res


@app.route('/start_task1')
def start_task1():
    values = {"arg1": "aa4", "arg2": "aa3"}

    task = task1.delay(values)
    return jsonify({"task_id": task.id}), 202



@app.route('/get_task_result/<task_id>')
def get_task_result(task_id):
    task_result = AsyncResult(task_id, app=celery)
    if task_result.ready():
        return jsonify(task_result.get())
    else:
        return jsonify({"status": "pending"})
    


if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='0.0.0.0', port=5000, debug=False)
