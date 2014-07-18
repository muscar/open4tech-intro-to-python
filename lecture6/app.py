import db

from db.models import LogEntry
from datetime import datetime as dt
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/logs')
def logs():
    with db.session_scope() as session:
        entries = session.query(LogEntry).order_by(LogEntry.created.desc()).all()
        return render_template('logs.html', entries=entries)


@app.route('/log', methods=['GET', 'POST'])
def log(name=None):
    if request.method == 'GET':
        return render_template('log.html')
    with db.session_scope() as session:
        session.add(LogEntry(level=request.form['level'],
                             created=dt.now(),
                             message=request.form['message']))
        session.commit()
        return redirect(url_for('logs'))


@app.teardown_appcontext
def shutdown_session(exception=None):
    with db.session_scope() as session:
        session.remove()


if __name__ == '__main__':
    db.init()
    app.run()
