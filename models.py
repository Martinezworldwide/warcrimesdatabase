from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    address = db.Column(db.String(500))
    website = db.Column(db.String(200))
    founded_date = db.Column(db.Date)
    founder = db.Column(db.String(200))
    headquarters = db.Column(db.String(200))
    type = db.Column(db.String(100))  # e.g., "Military Contractor", "Government Agency", etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    location = db.Column(db.String(200))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    organization = db.relationship('Organization', backref=db.backref('incidents', lazy=True))
    status = db.Column(db.String(100))  # e.g., "Under Investigation", "Proven", "Disputed"
    source = db.Column(db.String(500))  # URL or reference to source
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.String(500))
    document_type = db.Column(db.String(100))  # e.g., "Report", "Legal Document", "News Article"
    incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'))
    incident = db.relationship('Incident', backref=db.backref('documents', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 