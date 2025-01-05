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
        'description': 'Developing greener methods for gold recovery and adsorption; Gold separation from almost 16 other elements in WPCBs, or waste printed circuit boards, has been a recent intriguing research area, as the amount of WPCBs are increasing due to the advancement of AI and other techs. ',
        'image_url': '/static/img/gold_adsorption.jpg',
        'details': ['Studied adsorption capacity under different conditions.',
                    'Optimized kinetics and selectivity for maximum adsorption.',
                    'Evaluated the environmental impact of the process.',
                    'considering differnt leaching media for adospriton of gold using rGO'],
        'images': ['/static/img/gold-1.jpg','/static/img/gold-4.jpg','/static/img/gold-2.jpg','/static/img/gold-3.jpg','/static/img/gold-5.jpg','/static/img/gold-6.jpg']
    },
    {
        'id': 2,
        'title': 'Microwave assisted leaching of rare earth elements (REEs) using organic acids',
        'description': 'Transforming industrial waste, like red mud, into something valuable—A microwave-assisted approach. Red mud is a reddish residue of the Bayer process for producing alumina. This waste is generated in millions of tons each year, forcing the industries to find effective strategies to manage it. Such a massive, yet precious byproduct can be reach in some REEs like scandium and yttrium. Microwave technique can also be a promising method for selective heating and fast leaching of desirable components which is investigated in this project.',
        'image_url': '/static/img/microwave_redmud.jpg',
        'details': ['Optimized process for selective REE leaching.',
                    'Reduced environmental impact compared to conventional methods due to lower and greener acid usage.',
                    'Established a workflow for scalable recovery.',
                    "figuring out the mechanism beneath microwave assisted leaching"],
        'images': ['/static/img/mw-1.jpg','/static/img/mw-3.png','/static/img/xrd-redmud.png']

    },
    {
        "id": 3,
        "title": "Electrolyte recovery and PVDF removal from spent Li-ion batteries",
        "description": "Recycling Li-ion batteries by recovering electrolytes to support the circular economy, and manage the toxic chemicals involved. Li-ion battery electrolytes are usually made of some carbonate solvents and a Li-salt (typically LiPF6). The salt can highly react with moisture and water, producing HF gas as an undesirable product. Plus, carbonates have toxicity to some extend.",
        "image_url": "static/img/battery.jpg",
        "details": [
            "Developed methods to separate and purify electrolytes.",
            "Investigated the effects of different solvents on recovery efficiency.",
            "Ongoing research for industrial scalability.",
            
        ],
        'images': ['/static/img/hero4.jpg',"/static/img/battery.jpg",'/static/img/li-1.jpg']
    },
    {
        "id": 4,
        "title": "REEs separation using rGO - Nd magnet recycling ",
        "description": "Extracting REEs(Rare earth elements) from Nd magnets followed by purification through adsorption techniques: REEs are critical for manufacturing of high-tech devices, such as next-gen LED screens, aerospace equipment, and electric vehicles. Nd magnets that are out of order can be a potentially great secondary source for REEs supply. However, separation of these elements, either from impurities or from each other has always been a mindboggling challenge. In this project, we are experimenting with a graphene-based adsorbent designed to separate REEs from major impurities such as iron and copper. ",
        "image_url": "static/img/nd_magnet.png",
        "details": [
            "Optimized process for selective REE leaching.",
            "investigating different graphene oxide based adsorbents for separation if REEs",
            "Ongoing research for industrial scalability."
        ],
        'images': ['/static/img/magnet-1.jpg',"/static/img/magnet-2.jpg",'/static/img/hero5.jpg']
    },
    {
        "id": 5,
        "title": "Microwave assisted alkaline leaching of monazite",
        "description": "Finding ways to selectively leach REEs from monazite concentrates. Diversifying supply chains for critical materials is more important than ever. What excites me most is the potential to see these ideas making a real difference, not just in labs but in the world.",
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
        "description": "Exploring new ideas in water treatment, an area I feel passionate about given its impact on communities.",
        "image_url": "static/img/watertreat.jpg",
        "details": [
            "Evaluating graphene based adsorbents for heavy metal removal from waste waters ",
            "Reduced environmental impact compared to conventional methods.",
            "Trying to find an adsorbent that favours the circular economy with the ability of easy regeneration "
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
