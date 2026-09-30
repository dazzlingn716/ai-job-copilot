import os

from flask import Flask, render_template, request

from job_copilot import analyse_match


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/analyse")
def analyse():
    profile = request.form.get("profile", "")
    job_description = request.form.get("job_description", "")

    try:
        result = analyse_match(profile, job_description)
    except ValueError as exc:
        return render_template(
            "index.html",
            error=str(exc),
            profile=profile,
            job_description=job_description,
        ), 400

    return render_template(
        "result.html",
        result=result,
        profile=profile,
        job_description=job_description,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        debug=os.getenv("FLASK_DEBUG") == "1",
    )

