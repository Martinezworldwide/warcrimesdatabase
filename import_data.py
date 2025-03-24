from app import app, db
from models import Organization, Incident
from datetime import datetime
import os

def import_sample_data():
    with app.app_context():
        # Create database tables
        db.create_all()

        # Sample organizations with detailed information
        organizations = [
            {
                'name': 'Lockheed Martin',
                'description': 'Global aerospace, arms, defense, information security, and technology corporation. One of the world\'s largest defense contractors.',
                'address': '6801 Rockledge Drive, Bethesda, MD 20817, United States',
                'website': 'https://www.lockheedmartin.com',
                'founded_date': datetime(1995, 3, 15),
                'founder': 'Formed through the merger of Lockheed Corporation and Martin Marietta',
                'headquarters': 'Bethesda, Maryland, United States',
                'type': 'Defense Contractor'
            },
            {
                'name': 'Raytheon Technologies',
                'description': 'Major aerospace and defense company that provides advanced systems and services for commercial, military, and government customers worldwide.',
                'address': '870 Winter Street, Waltham, MA 02451, United States',
                'website': 'https://www.raytheon.com',
                'founded_date': datetime(2020, 4, 3),
                'founder': 'Formed through the merger of Raytheon Company and United Technologies Corporation',
                'headquarters': 'Waltham, Massachusetts, United States',
                'type': 'Defense Contractor'
            },
            {
                'name': 'Northrop Grumman',
                'description': 'Global aerospace and defense technology company providing innovative systems, products, and solutions in autonomous systems, cyber, C4ISR, strike, and logistics.',
                'address': '2980 Fairview Park Drive, Falls Church, VA 22042, United States',
                'website': 'https://www.northropgrumman.com',
                'founded_date': datetime(1994, 1, 1),
                'founder': 'Formed through the merger of Northrop Corporation and Grumman Corporation',
                'headquarters': 'Falls Church, Virginia, United States',
                'type': 'Defense Contractor'
            },
            {
                'name': 'Boeing Defense, Space & Security',
                'description': 'Division of The Boeing Company that provides military aircraft, weapons, and strategic defense and intelligence systems.',
                'address': '929 Long Bridge Drive, Arlington, VA 22202, United States',
                'website': 'https://www.boeing.com/defense',
                'founded_date': datetime(2002, 1, 1),
                'founder': 'Division of The Boeing Company',
                'headquarters': 'Arlington, Virginia, United States',
                'type': 'Defense Contractor'
            },
            {
                'name': 'General Dynamics',
                'description': 'Aerospace and defense company that provides business aviation, combat vehicles, weapons systems, munitions, shipbuilding, and technology products and services.',
                'address': '11011 Sunset Hills Road, Reston, VA 20190, United States',
                'website': 'https://www.gd.com',
                'founded_date': datetime(1952, 2, 21),
                'founder': 'John Philip Holland',
                'headquarters': 'Reston, Virginia, United States',
                'type': 'Defense Contractor'
            }
        ]

        # Add organizations to database
        for org_data in organizations:
            org = Organization(**org_data)
            db.session.add(org)
        
        # Sample incidents
        incidents = [
            {
                'title': 'Yemen Civilian Casualties',
                'description': 'Reports of civilian casualties resulting from military operations in Yemen',
                'date': datetime(2023, 1, 15),
                'location': 'Yemen',
                'organization_id': 1,  # Lockheed Martin
                'status': 'Under Investigation',
                'source': 'UN Human Rights Council Report'
            },
            {
                'title': 'Syria Conflict Involvement',
                'description': 'Allegations of weapons systems being used in civilian areas',
                'date': datetime(2023, 3, 20),
                'location': 'Syria',
                'organization_id': 2,  # Raytheon
                'status': 'Under Investigation',
                'source': 'Human Rights Watch Report'
            }
        ]

        # Add incidents to database
        for inc_data in incidents:
            inc = Incident(**inc_data)
            db.session.add(inc)

        # Commit all changes
        db.session.commit()
        print("Sample data imported successfully!")

if __name__ == '__main__':
    import_sample_data() 