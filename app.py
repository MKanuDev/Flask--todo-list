from flask import Flask, render_template, request, redirect
# "import" means bring in tools someone else already built.
app = Flask(__name__)
# This creates our website and calls it "app".
tasks = []
# This is a list that will hold all of our tasks.
@app.route("/")
# This is a decorator. It tells Flask what URL should trigger our function.
def home():
    return render_template("index.html", tasks=tasks)
    # This function returns the contents of index.html when someone visits the root URL.
@app.route("/add", methods=["POST"])
# When someone visits the /add URL with a POST request, this function will be called.
def add():
    task = request.form.get("task")
    # This gets the value of the "task" input from the form.
    if task:
        tasks.append(task)
        # If the task is not empty, add it to the list of tasks.
    return redirect("/")
    # After adding the task, redirect back to the home page.
@app.route("/delete/<int:task_id>")
# When someone visits the /delete/<task_id> URL, this function will be called.
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
    # This runs the app in debug mode, which means it will automatically reload if we make changes to the code.
