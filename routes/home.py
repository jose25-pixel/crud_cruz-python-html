from flask import Blueprint, render_template, request, redirect, url_for, flash
from store import data, get_next_id

home_bp = Blueprint("home", __name__)

# READ
@home_bp.route("/", methods=["GET"])
def home():
    records = list(data.values())
    return render_template("home.html", records=records)


# CREATE
@home_bp.route("/create", methods=["POST"])
def create():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    role = request.form.get("role", "").strip()

    if not name or not email:
        flash("Name and email are required", "error")
        return redirect(url_for("home.home"))

    record_id = get_next_id()

    data[record_id] = {
        "id": record_id,
        "name": name,
        "email": email,
        "role": role
    }

    flash(f'Record "{name}" created successfully.', "success")
    return redirect(url_for("home.home"))


# EDIT
@home_bp.route("/edit/<record_id>", methods=["GET"])
def edit(record_id):

    record = data.get(record_id)

    if not record:
        flash("Record not found", "error")
        return redirect(url_for("home.home"))

    records = list(data.values())
    return render_template("home.html", records=records, editing=record)


# UPDATE
@home_bp.route("/update/<record_id>", methods=["POST"])
def update(record_id):

    if record_id not in data:
        flash("Record not found", "error")
        return redirect(url_for("home.home"))

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    role = request.form.get("role", "").strip()

    if not name or not email:
        flash("Name and email are required", "error")
        return redirect(url_for("home.edit", record_id=record_id))

    data[record_id].update({
        "name": name,
        "email": email,
        "role": role
    })

    flash(f'Record "{name}" updated successfully.', "success")
    return redirect(url_for("home.home"))


# DELETE
@home_bp.route("/delete/<record_id>", methods=["POST"])
def delete(record_id):

    record = data.pop(record_id, None)

    if record:
        flash(f'Record "{record["name"]}" deleted.', "success")
    else:
        flash("Record not found", "error")

    return redirect(url_for("home.home"))

    
