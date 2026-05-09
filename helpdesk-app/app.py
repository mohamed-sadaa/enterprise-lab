from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import db, Ticket
from datetime import datetime
import subprocess
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpdesk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

SERVERS = [
    {'name': 'FreeIPA', 'ip': '192.168.10.10', 'role': 'Auth Server'},
    {'name': 'Samba', 'ip': '192.168.10.20', 'role': 'File Server'},
    {'name': 'ELK Stack', 'ip': '192.168.10.30', 'role': 'Log Server'},
]

def ping_server(ip):
    try:
        result = subprocess.run(
            ['ping', '-c', '1', '-W', '1', ip],
            capture_output=True, timeout=3
        )
        return result.returncode == 0
    except:
        return False

def get_elk_logs(size=10):
    try:
        r = requests.get(
            'http://192.168.10.30:9200/filebeat-*/_search',
            json={"query": {"match_all": {}},
                  "sort": [{"@timestamp": {"order": "desc"}}],
                  "size": size},
            timeout=3
        )
        hits = r.json().get('hits', {}).get('hits', [])
        return [h['_source'] for h in hits]
    except:
        return []

@app.route('/')
def dashboard():
    servers = []
    for s in SERVERS:
        s['status'] = 'Online' if ping_server(s['ip']) else 'Offline'
        servers.append(s)
    total = Ticket.query.count()
    open_tickets = Ticket.query.filter_by(status='Open').count()
    in_progress = Ticket.query.filter_by(status='In Progress').count()
    closed = Ticket.query.filter_by(status='Closed').count()
    recent = Ticket.query.order_by(Ticket.created_at.desc()).limit(5).all()
    logs = get_elk_logs(5)
    return render_template('dashboard.html',
        servers=servers, total=total,
        open_tickets=open_tickets, in_progress=in_progress,
        closed=closed, recent_tickets=recent, logs=logs)

@app.route('/tickets')
def tickets():
    all_tickets = Ticket.query.order_by(Ticket.created_at.desc()).all()
    return render_template('tickets.html', tickets=all_tickets)

@app.route('/tickets/new', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        ticket = Ticket(
            title=request.form['title'],
            description=request.form['description'],
            priority=request.form['priority'],
            assigned_to=request.form['assigned_to']
        )
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('tickets'))
    return render_template('new_ticket.html')

@app.route('/tickets/<int:id>/update', methods=['POST'])
def update_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    ticket.status = request.form['status']
    ticket.updated_at = datetime.utcnow()
    db.session.commit()
    return redirect(url_for('tickets'))

@app.route('/tickets/<int:id>/delete', methods=['POST'])
def delete_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    return redirect(url_for('tickets'))

@app.route('/api/servers')
def api_servers():
    servers = []
    for s in SERVERS:
        s['status'] = 'Online' if ping_server(s['ip']) else 'Offline'
        servers.append(s)
    return jsonify(servers)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
