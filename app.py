from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для хранения информации о проектах
projects = []


@app.route('/')
def index():
    return render_template('index.html', projects=projects)


@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        project_name = request.form['project_name']
        performer = request.form['performer']
        producer = request.form['producer']
        client_company = request.form['client_company']
        work_date = request.form['work_date']

        # Добавление нового проекта в список
        projects.append({
            'project_name': project_name,
            'performer': performer,
            'producer': producer,
            'client_company': client_company,
            'work_date': work_date
        })

        return redirect(url_for('index'))

    return render_template('add_project.html')  # GET-запрос


@app.route('/calculator')
def calculator():
    return redirect("https://www.kontur-extern.ru/info/calculator-sno")


if __name__ == '__main__':
    app.run(debug=True)