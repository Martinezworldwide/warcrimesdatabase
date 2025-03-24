from flask import Flask, render_template, request, jsonify
from models import db, Organization, Incident, Document
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warcrimes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/organizations', methods=['GET'])
def get_organizations():
    organizations = Organization.query.all()
    return jsonify([{
        'id': org.id,
        'name': org.name,
        'description': org.description,
        'address': org.address,
        'website': org.website,
        'founded_date': org.founded_date.isoformat() if org.founded_date else None,
        'founder': org.founder,
        'headquarters': org.headquarters,
        'type': org.type
    } for org in organizations])

@app.route('/api/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([{
        'id': inc.id,
        'title': inc.title,
        'description': inc.description,
        'date': inc.date.isoformat() if inc.date else None,
        'location': inc.location,
        'organization_id': inc.organization_id,
        'status': inc.status,
        'source': inc.source
    } for inc in incidents])

@app.route('/api/organizations', methods=['POST'])
def add_organization():
    data = request.json
    org = Organization(
        name=data['name'],
        description=data.get('description'),
        address=data.get('address'),
        website=data.get('website'),
        founded_date=datetime.strptime(data['founded_date'], '%Y-%m-%d').date() if data.get('founded_date') else None,
        founder=data.get('founder'),
        headquarters=data.get('headquarters'),
        type=data.get('type')
    )
    db.session.add(org)
    db.session.commit()
    return jsonify({'id': org.id, 'message': 'Organization added successfully'})

@app.route('/api/incidents', methods=['POST'])
def add_incident():
    data = request.json
    inc = Incident(
        title=data['title'],
        description=data.get('description'),
        date=datetime.strptime(data['date'], '%Y-%m-%d').date() if data.get('date') else None,
        location=data.get('location'),
        organization_id=data.get('organization_id'),
        status=data.get('status'),
        source=data.get('source')
    )
    db.session.add(inc)
    db.session.commit()
    return jsonify({'id': inc.id, 'message': 'Incident added successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 