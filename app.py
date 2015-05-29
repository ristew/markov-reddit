from flask import Flask, g, render_template
import commentgetterthing as cgt
import thread

app = Flask(__name__)

app.config.update(dict(
    DATABASE='',
    DEBUG=True,
    SECRET_KEY='dev',
    USERNAME='admin',
    PASSWORD='default'
    ))

cgt.m.addfile('austen-emma.txt')

try:
    thr = thread.start_new_thread(cgt.add_comments, ('all'))
except:
    pass

@app.route('/')
def front_page():
    return render_template('words.html', words=cgt.m.gen(50))
"""
@app.route('/<sub>')
def sub_page(sub):
    thr.exit()
    thr = thread.start_new_thread(cgt.add_comments, (sub))
"""
app.run()
