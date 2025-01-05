from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For flash messages


# app.config['MAIL_USERNAME'] = os.getenv('SMTP_USERNAME')
# app.config['MAIL_PASSWORD'] = os.getenv('SMTP_PASSWORD')
# SMTP Configuration
app.config['MAIL_SERVER'] = 'smtp.yourhosting.com'  # Replace with your SMTP server address
app.config['MAIL_PORT'] = 465  # Use 465 for SSL or 587 for TLS
app.config['MAIL_USE_TLS'] = False  # False if using SSL
app.config['MAIL_USE_SSL'] = True  # True if using SSL
app.config['MAIL_USERNAME'] = 'your-email@yourdomain.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = ('Your Name', 'your-email@yourdomain.com')

mail = Mail(app)

# Sample data for projects
projects = [
    {
        'id': 1,
        'title': 'Gold adsorption and recovery using reduced graphene oxide',
        'description': 'This project focuses on the adsorption of gold using rGO synthesized in the lab.',
        'image_url': '/static/img/gold_adsorption.jpg',
        'details': ['Studied adsorption capacity under different conditions.',
                    'Optimized pH and temperature for maximum adsorption.',
                    'Evaluated the environmental impact of the process.'],
        'images': ['/static/img/gold-1.jpg','/static/img/gold-4.jpg','/static/img/gold-2.jpg','/static/img/gold-3.jpg','/static/img/gold-5.jpg','/static/img/gold-6.jpg']
    },
    {
        'id': 2,
        'title': 'Microwave assisted leaching of rare earth elements (REEs) using organic acids',
        'description': 'Recovery of electrolytes from used Li-ion batteries for sustainable reuse.',
        'image_url': '/static/img/microwave_redmud.jpg',
        'details': ['Developed methods to separate and purify electrolytes.',
                    'Investigated the effects of different solvents on recovery efficiency.',
                    'Established a workflow for scalable recovery.'],
        'images': ['/static/img/mw-1.jpg','/static/img/mw-3.png','/static/img/xrd-redmud.png']

    },
    {
        "id": 3,
        "title": "Electrolyte recovery and PVDF removal from spent Li-ion batteries",
        "description": "Microwave-assisted leaching for REE extraction.",
        "image_url": "static/img/battery.jpg",
        "details": [
            "Optimized process for selective REE leaching.",
            "Reduced environmental impact compared to conventional methods.",
            "Ongoing research for industrial scalability."
        ],
        'images': ['/static/img/hero4.jpg',"/static/img/battery.jpg",'/static/img/li-1.jpg']
    },
    {
        "id": 4,
        "title": "REEs separation using rGO - Nd magnet recycling ",
        "description": "Microwave-assisted leaching for REE extraction.",
        "image_url": "static/img/nd_magnet.png",
        "details": [
            "Optimized process for selective REE leaching.",
            "Reduced environmental impact compared to conventional methods.",
            "Ongoing research for industrial scalability."
        ],
        'images': ['/static/img/magnet-1.jpg',"/static/img/magnet-2.jpg",'/static/img/hero5.jpg']
    },
    {
        "id": 5,
        "title": "Microwave assisted alkaline leaching of monazite",
        "description": "Microwave-assisted leaching for REE extraction.",
        "image_url": "static/img/Monazite.jpg",
        "details": [
            "Optimized process for selective REE leaching.",
            "Reduced environmental impact compared to conventional methods.",
            "Ongoing research for industrial scalability."
        ]
    },
    {
        
        "id": 6,
        "title": "Water treatment and heavy metal ions removal using graphene-oxide based adsorbents",
        "description": "Microwave-assisted leaching for REE extraction.",
        "image_url": "static/img/watertreat.jpg",
        "details": [
            "Optimized process for selective REE leaching.",
            "Reduced environmental impact compared to conventional methods.",
            "Ongoing research for industrial scalability."
        ]
        
    }
    # Add more projects here
]

works = [
    {
        "id": 1,
        'title': "Teacher assistant at University of Tehran - Processes of Hydro , bio , electro metallurgy course",
        'description':"Currently, I assist new students in gaining hands-on experience solving real research problems and performing calculations related to recycling and metal leaching through different techniques. I also teach thermodynamic calculations using software like HSC and Medusa (drawing Pourbaix diagrams, finding and interpreting chemical reactions, drawing species diagrams, etc.). " ,
        "place": "University of Tehran",
        "link":"https://ut.ac.ir/fa" ,
        'date': "Oct 2024 - Jan 2025"
    },
    {
        "id": 2,
        'title': "Research assistant at recycling laboratory - University of Tehran",
        'description':" I am always honored to assist novice students and researchers, helping them learn how to work with various lab equipment while adhering to safety protocols. Additionally, I am responsible for managing lab resources and maintaining equipment. " ,
        "place": "Recycling Lab",
        "link":"https://meteng.ut.ac.ir/lab-23" ,
        'date': "Aug 2024 - Jan 2025"
    },
    {
        "id": 3,
        'title': "Laboratory operator at Parsian metallurgy center",
        'description':"  After learning the basics of spark emission spectroscopy (SES) at Fooladrizan, I joined Parsian Lab as an SES operator. My role involved identifying the grade of each sample, and I had the opportunity to work with an Oxford spectroscopy instrument capable of analyzing copper-based alloys, steels, and cast iron (excluding ductile iron). Sample preparation, including grinding and polishing, was also necessary. The chemical composition was then used to match the compounds with AISI, DIN, or other standards." ,
        "place": "Parsian metallurgy center",
        "link":"https://pmclab.ir/" ,
        'date': "Oct 2021 - Feb 2022"
    },
    {
        "id": 4,
        'title': "Internship at Fooladrizan co.",
        'description':" Fooladrizan Complex has several units for casting steel and cast iron products. During this internship, I worked in various units, including molding, assembly, melting, heat treatment, and quality control.My responsibilities primarily involved proper molding using CO2 gas, making cores, furnace charge calculations, machining the final product, and controlling the alloy composition using spark emission spectroscopy." ,
        "place": "Fooladrizaan",
        "link":"http://fouladrizan.com/" ,
        'date': "Jun 2021 - Aug 2021"
    }
    
    
   
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, works=works)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('details.html', project=project)
    else:
        return "Project not found", 404



@app.route("/contact", methods=["POST"])
def contact():
    try:
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message_content = request.form['message']

        # Construct the email
        subject = f"my-portfolio-{name}-{datetime.now().strftime('%Y-%m-%d')}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"

        # Send the email
        msg = Message(subject=subject, sender=email, recipients=['your_email@gmail.com'])
        msg.body = body
        mail.send(msg)

        flash("Message sent successfully!", "success")
    except Exception as e:
        print(e)
        flash("Failed to send message. Please try again.", "danger")
    
    return redirect("/#contact")




if __name__ == '__main__':
    app.run(debug=True)
