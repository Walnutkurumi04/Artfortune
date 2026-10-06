from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    services = [
        {
            "icon": "🎨",
            "title": "Peinture & décoration",
            "description": "Peinture intérieure et extérieure, décoration murale et finition soignée pour donner du caractère à vos espaces.",
            "color": "violet"
        },
        {
            "icon": "📐",
            "title": "Conception de plans",
            "description": "Conception et préparation de plans adaptés à vos projets de construction, rénovation et aménagement.",
            "color": "pink"
        },
        {
            "icon": "🏠",
            "title": "Staff & plafonds",
            "description": "Création et installation de plafonds et éléments en staff pour des intérieurs élégants et modernes.",
            "color": "yellow"
        },
        {
            "icon": "🚿",
            "title": "Plomberie",
            "description": "Installation, réparation et aménagement des réseaux de plomberie pour vos bâtiments.",
            "color": "green"
        },
        {
            "icon": "▦",
            "title": "Carrelage",
            "description": "Pose de carrelage pour les sols et murs avec une attention particulière portée aux finitions.",
            "color": "pink"
        },
        {
            "icon": "📹",
            "title": "Caméras de surveillance",
            "description": "Installation de systèmes de vidéosurveillance pour renforcer la sécurité de vos maisons, commerces et bâtiments.",
            "color": "violet"
        },
        {
            "icon": "⚡",
            "title": "Électricité bâtiment",
            "description": "Travaux d'installation et d'aménagement électrique pour bâtiments résidentiels et professionnels.",
            "color": "yellow"
        },
        {
            "icon": "🪚",
            "title": "Menuiserie",
            "description": "Travaux de menuiserie et réalisation d'éléments adaptés à vos besoins et à votre intérieur.",
            "color": "green"
        }
    ]

    projects = [
        {
            "image": "projet-1.jpg",
            "title": "Peinture intérieure",
            "category": "Peinture & décoration"
        },
        {
            "image": "projet-2.jpg",
            "title": "Plafond décoratif",
            "category": "Staff & plafond"
        },
        {
            "image": "projet-3.jpg",
            "title": "Finition murale",
            "category": "Décoration"
        },
        {
            "image": "projet-4.jpg",
            "title": "Pose de carrelage",
            "category": "Carrelage"
        },
        {
            "image": "projet-5.jpg",
            "title": "Installation électrique",
            "category": "Électricité bâtiment"
        },
        {
            "image": "projet-6.jpg",
            "title": "Aménagement",
            "category": "Menuiserie"
        }
    ]

    return render_template(
        "index.html",
        services=services,
        projects=projects
    )

if __name__ == "__main__":
    app.run(debug=True)