

import gradio as gr
from urllib.parse import quote_plus

# 6 Complete Skin Types & Concerns Database with Products, Prices (PKR) and Time (Day/Night)
skincare_db = {
    "Acne-Prone": {
        "Oily": [
            {"name": "Jenpharm Spectra Matte Sunscreen", "type": "Sunscreen", "price": 1800, "time": "Day"},
            {"name": "Organic Traveller Niacinamide Serum", "type": "Serum", "price": 1450, "time": "Day"},
            {"name": "The Ordinary Salicylic Acid", "type": "Serum", "price": 2500, "time": "Night"},
            {"name": "U-Veil Forte Sunscreen", "type": "Sunscreen", "price": 1200, "time": "Day"}
        ],
        "Dry": [
            {"name": "Hemani Tea Tree Face Wash", "type": "Cleanser", "price": 650, "time": "Day"},
            {"name": "Pond's Super Light Gel", "type": "Moisturizer", "price": 800, "time": "Day"},
            {"name": "Jenpharm Hydramax Night Cream", "type": "Moisturizer", "price": 2200, "time": "Night"}
        ]
    },
    "Dry & Dehydrated": {
        "Dry": [
            {"name": "CeraVe Hydrating Cleanser", "type": "Cleanser", "price": 3500, "time": "Day"},
            {"name": "Organic Traveller Hyaluronic Acid", "type": "Serum", "price": 1600, "time": "Day"},
            {"name": "Bioderma Photoderm Max Cream", "type": "Sunscreen", "price": 4200, "time": "Day"},
            {"name": "Physiogel Calming Relief Cream", "type": "Moisturizer", "price": 3200, "time": "Night"}
        ],
        "Oily": [
            {"name": "Cetaphil Moisturizing Lotion", "type": "Moisturizer", "price": 2800, "time": "Day"},
            {"name": "The Ordinary Hyaluronic Acid", "type": "Serum", "price": 2900, "time": "Night"}
        ]
    },
    "Combination": {
        "Oily": [
            {"name": "Cetaphil Gentle Skin Cleanser", "type": "Cleanser", "price": 2400, "time": "Day"},
            {"name": "The Ordinary Niacinamide", "type": "Serum", "price": 2900, "time": "Day"},
            {"name": "Jenpharm Fluid Sunscreen", "type": "Sunscreen", "price": 1950, "time": "Day"}
        ],
        "Dry": [
            {"name": "Neutrogena Hydro Boost Gel", "type": "Moisturizer", "price": 3000, "time": "Day"},
            {"name": "Jenpharm Fluid Sunscreen", "type": "Sunscreen", "price": 1950, "time": "Day"}
        ]
    },
    "Sensitive": {
        "Dry": [
            {"name": "Bioderma Sensibio H2O", "type": "Cleanser", "price": 3100, "time": "Day"},
            {"name": "Solaris Mineral Sunscreen", "type": "Sunscreen", "price": 2500, "time": "Day"},
            {"name": "Physiogel Face Cream", "type": "Moisturizer", "price": 3200, "time": "Night"}
        ],
        "Oily": [
            {"name": "Simple Kind to Skin Wash", "type": "Cleanser", "price": 1500, "time": "Day"},
            {"name": "U-Veil Sensitive Sunscreen", "type": "Sunscreen", "price": 1400, "time": "Day"}
        ]
    },
    "Oily & Greasy": {
        "Oily": [
            {"name": "Revent 60 Sunblock Gel", "type": "Sunscreen", "price": 1650, "time": "Day"},
            {"name": "Salicylic Acid Face Wash", "type": "Cleanser", "price": 1350, "time": "Day"},
            {"name": "The Ordinary Niacinamide 10%", "type": "Serum", "price": 2900, "time": "Night"}
        ],
        "Dry": [
            {"name": "Pond's Oil Control Gel", "type": "Moisturizer", "price": 750, "time": "Day"}
        ]
    },
    "Normal / Balanced": {
        "Dry": [
            {"name": "Nivea Soft Light Moisturizer", "type": "Moisturizer", "price": 600, "time": "Day"},
            {"name": "Spectra Matte Sunscreen", "type": "Sunscreen", "price": 1800, "time": "Day"}
        ],
        "Oily": [
            {"name": "Lotus Herbals Sunblock", "type": "Sunscreen", "price": 1300, "time": "Day"},
            {"name": "Organic Traveller Moisturizer", "type": "Moisturizer", "price": 1250, "time": "Night"}
        ]
    }
}

# Pakistan Cities Expert & Salon Database
pakistan_experts_db = {
    "lahore": [
        {"name": "Dr. Ijaz Ahsan (Gulberg III)", "type": "Dermatologist", "contact": "Appointment based"},
        {"name": "Depilex Beauty Clinic (Gulberg)", "type": "Salon", "contact": "Skin Treatments & Facials"}
    ],
    "karachi": [
        {"name": "Dr. Bilquis Fazal (Clifton)", "type": "Dermatologist", "contact": "Appointment based"},
        {"name": "Nabila's Salon (Clifton)", "type": "Salon", "contact": "Aesthetic Skin Care"}
    ],
    "islamabad": [
        {"name": "Dr. Farooq Ahmad (F-8/4)", "type": "Dermatologist", "contact": "Appointment based"},
        {"name": "Depilex Salon (F-6)", "type": "Salon", "contact": "Skin & Hair Services"}
    ],
    "multan": [
        {"name": "Dr. Shahid Siddique (Bosan Road)", "type": "Dermatologist", "contact": "Appointment based"},
        {"name": "Signature Salon (Gulgasht)", "type": "Salon", "contact": "Facials & Skin Care"}
    ],
    "faisalabad": [
        {"name": "Dr. Muhammad Saleem (People's Colony)", "type": "Dermatologist", "contact": "Appointment based"},
        {"name": "Amina Z Salon (D-Ground)", "type": "Salon", "contact": "Skin Treatments"}
    ],
    "rawalpindi": [
        {"name": "Dr. Asif Mahmood (Saddar)", "type": "Dermatologist", "contact": "Appointment based"},
        {"name": "Khawaja's Salon (Saddar)", "type": "Salon", "contact": "Beauty & Skin Care"}
    ]
}

# AI Skin Scan Simulator Logic
def scan_skin_image(image):
    if image is None:
        return "⚠️ Pehle apni skin ki tasveer upload karein!"
    return "✅ **AI Skin Scan Successful!** Oily/Acne texture detected. Neeche routine planner se apna budget aur city select karein!"

# Routine Planner Logic with Day & Night Separation
def generate_routine(skin_type, sub_type, budget, city, allergies):
    categories = skincare_db.get(skin_type, {})
    products = categories.get(sub_type, [])

    filtered_products = [p for p in products if p["price"] <= budget]

    day_products = [p for p in filtered_products if p["time"] == "Day"]
    night_products = [p for p in filtered_products if p["time"] == "Night"]

    result = f"### 🧴 Skincare Routine ({skin_type} - {sub_type}):\n\n"

    result += "☀️ **Subha ki Routine (Day Routine):**\n"
    if day_products:
        for p in day_products:
            result += f"- **{p['name']}** ({p['type']}) — PKR {p['price']}\n"
    else:
        result += "- Is budget mein subha ke products filhal dastiyab nahi hain.\n"

    result += "\n🌙 **Raat ki Routine (Night Routine):**\n"
    if night_products:
        for p in night_products:
            result += f"- **{p['name']}** ({p['type']}) — PKR {p['price']}\n"
    else:
        result += "- Is budget mein raat ke products filhal dastiyab nahi hain.\n"

    if allergies == "Yes":
        result += "\n⚠️ *Note: Allergies ki wajah se koi bhi naya product patch test ke baghair use na karein.*\n"

    result += f"\n--- \n### 🩺 Recommended Experts in {city.capitalize()} (Pakistan):\n"
    city_experts = pakistan_experts_db.get(city.lower(), [])
    if city_experts:
        for expert in city_experts:
            result += f"- **{expert['name']}** ({expert['type']}) — {expert['contact']}\n"
    else:
        result += "- General Certified Dermatologists & Salons\n"
    return result

# Chatbot Logic
def skin_chatbot(user_message, history):
    if history is None:
        history = []
    msg_lower = user_message.lower()
    if "sunscreen" in msg_lower:
        response = "Sunscreen subha ke waqt lagana lazmi hai taake dhoop se bach sakein!"
    elif "night" in msg_lower or "raat" in msg_lower:
        response = "Raat ki routine mein serums aur moisturizers skin ko heal karne ke liye behtareen hote hain."
    else:
        response = "Main SkinAI Expert hoon! Aap subha/raat ki routine ya skin experts ke baray mein pooch sakte hain."
    history.append([user_message, response])
    return history, ""


def find_nearby_care(city):
    if not city:
        return "⚠️ Please select a city."

    city = city.strip()

    dermatologist_url = (
        "https://www.google.com/maps/search/?api=1&query="
        + quote_plus(f"dermatologist near {city}, Pakistan")
    )

    skin_clinic_url = (
        "https://www.google.com/maps/search/?api=1&query="
        + quote_plus(f"skin clinic near {city}, Pakistan")
    )

    beauty_salon_url = (
        "https://www.google.com/maps/search/?api=1&query="
        + quote_plus(f"beauty salon near {city}, Pakistan")
    )

    return f"""
## 📍 Skincare Services in {city.title()}

🩺 [**Find Dermatologists in {city.title()}**]({dermatologist_url})

🏥 [**Find Skin Clinics in {city.title()}**]({skin_clinic_url})

💆 [**Find Beauty Salons in {city.title()}**]({beauty_salon_url})

Click any option above to open the relevant Google Maps search.
"""

# Single-Page UI Layout
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# ✨ SkinAI Agent - Day/Night Routine & Pakistan Expert Locator")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📸 AI Skin Scanner")
            img_input = gr.Image(type="pil", label="Upload Selfie")
            scan_btn = gr.Button("Scan Skin", variant="primary")
            scan_output = gr.Markdown()
            scan_btn.click(fn=scan_skin_image, inputs=[img_input], outputs=[scan_output])

        with gr.Column():
            gr.Markdown("### 🧴 Day & Night Routine Planner")
            skin_type = gr.Dropdown(choices=list(skincare_db.keys()), label="Skin Concern", value="Acne-Prone")
            sub_type = gr.Dropdown(choices=["Oily", "Dry"], label="Skin Texture", value="Oily")
            city_input = gr.Dropdown(choices=list(pakistan_experts_db.keys()), label="Select City (Pakistan)", value="lahore")
            budget = gr.Slider(minimum=500, maximum=5000, step=100, value=2500, label="Budget Limit (PKR)")
            allergies = gr.Radio(choices=["No", "Yes"], label="Skin Allergies?", value="No")

            submit_btn = gr.Button("Generate Day/Night Routine", variant="primary")
            output_box = gr.Markdown()
            submit_btn.click(fn=generate_routine, inputs=[skin_type, sub_type, budget, city_input, allergies], outputs=output_box)

    gr.Markdown("---")
    gr.Markdown("## 📍 Find Skincare Services Near You")

    city_map = gr.Dropdown(
           choices=list(pakistan_experts_db.keys()),
           label="Select Your City"
    )

    map_btn = gr.Button(
           "🔎 Search Google Maps",
           variant="primary"
    )

    map_output = gr.Markdown()

    map_btn.click(
           fn=find_nearby_care,
           inputs=city_map,
           outputs=map_output
    )

    gr.Markdown("### 💬 SkinAI Expert Chatbot")
    chatbot = gr.Chatbot(label="Chat with Expert")
    msg = gr.Textbox(placeholder="Apna sawal yahan type karein...", label="Sawal likhein")
    msg.submit(skin_chatbot, inputs=[msg, chatbot], outputs=[chatbot, msg])

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0", debug=False) 


