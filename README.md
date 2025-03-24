# War Crimes Database

A comprehensive database and web interface for tracking organizations and incidents related to war crimes.

## Features

- Organization profiles with detailed information
- Incident tracking and documentation
- Document management system
- Search functionality
- Modern web interface

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python app.py
```

4. Access the web interface:
Open your browser and navigate to `http://localhost:5000`

## Database Structure

### Organizations
- Name
- Description
- Address
- Website
- Founded Date
- Founder
- Headquarters
- Type

### Incidents
- Title
- Description
- Date
- Location
- Organization (linked)
- Status
- Source

### Documents
- Title
- Description
- File Path
- Document Type
- Incident (linked)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 