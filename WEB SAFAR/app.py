from flask import Flask, request, jsonify, render_template
from flask import session, redirect

from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = "mysecret123"


# 🔹 MongoDB Connection (Local)
client = MongoClient("mongodb://localhost:27017")

db = client["eventdb"]
users_col = db["users"]
events_col = db["events"]


# 🔹 Admin Credentials (Demo Purpose)
ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASS = "1234"


# ==================================================
# 🔹 Landing Page (Beautiful UI)
# ==================================================
@app.route("/")
def home():
    return render_template("home.html")


# ==================================================
# 🔹 Dashboard Page
# ==================================================
@app.route("/dashboard")
def dashboard():

    event_count = events_col.count_documents({})
    user_count = users_col.count_documents({})

    return render_template(
        "dashboard.html",
        event_count=event_count,
        user_count=user_count
    )


# ==================================================
# 🔹 User Register API
# ==================================================
@app.route("/register", methods=["POST"])
def register():

    data = request.json

    print("REGISTER DATA:", data)   # Debug

    users_col.insert_one({
        "name": data["name"],
        "email": data["email"],
        "event": data["event"],
        "status": "pending"
    })

    return jsonify({"msg": "Registered Successfully"})


# ==================================================
# 🔹 Users List API (Admin)
# ==================================================
@app.route("/users")
def get_users():

    data = []

    for u in users_col.find({}, {"_id": 0}):
        data.append(u)

    return jsonify(data)


# ==================================================
# 🔹 Update Status API
# ==================================================
@app.route("/update", methods=["PUT"])
def update():

    data = request.json

    users_col.update_one(
        {"email": data["email"]},
        {"$set": {"status": data["status"]}}
    )

    return jsonify({"msg": "Status Updated"})


# ==================================================
# 🔹 Admin Dashboard
# ==================================================
@app.route("/admin")
def admin_page():

    if not session.get("admin"):
        return redirect("/login")

    all_users = list(users_col.find({}, {"_id": 0}))

    return render_template("admin.html", users=all_users)


# ==================================================
# 🔹 Create Event (Admin)
# ==================================================
@app.route("/create_event", methods=["POST"])
def create_event():

    data = request.json

    print("EVENT DATA:", data)   # 👈 Debug

    if not data:
        return jsonify({"msg":"No data received"}), 400

    events_col.insert_one({
        "title": data.get("title"),
        "date": data.get("date"),
        "desc": data.get("desc")
    })

    return jsonify({"msg": "Event Created Successfully"})



# ==================================================
# 🔹 Get Events API
# ==================================================
@app.route("/events")
def get_events():

    data = []

    for e in events_col.find({}, {"_id": 0}):
        data.append(e)

    return jsonify(data)


# ==================================================
# 🔹 Admin Login
# ==================================================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email == ADMIN_EMAIL and password == ADMIN_PASS:

            session["admin"] = True
            return redirect("/admin")

        else:
            return "Invalid Login ❌"

    return render_template("login.html")


# ==================================================
# 🔹 Logout
# ==================================================
@app.route("/logout")
def logout():

    session.pop("admin", None)
    return redirect("/login")


# ==================================================
# 🔹 Pages
# ==================================================
@app.route("/register_page")
def register_page():
    return render_template("index.html")


@app.route("/events_page")
def events_page():

    events = list(events_col.find({}, {"_id": 0}))

    return render_template("events.html", events=events)


# ==================================================
# 🔹 Run Server
# ==================================================
if __name__ == "__main__":
    app.run(debug=True)
