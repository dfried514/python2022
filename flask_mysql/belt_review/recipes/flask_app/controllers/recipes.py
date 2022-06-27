from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.recipe import Recipe

@app.route('/recipes/<int:id>')
def show_recipe(id):
    return render_template('recipe.html', recipe=Recipe.get_recipe_with_id(id))

@app.route('/recipes/new')
def new_recipe():
    if session['logged_in'] == True:
        return render_template('edit_recipe.html', title='Add New Recipe', form_function='create', recipe=Recipe.get_dummy_recipe())
    return redirect(url_for('index'))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if session['logged_in'] == True:
        return render_template('edit_recipe.html', title='Edit Recipe', form_function='update', recipe=Recipe.get_recipe_with_id(id))
    return redirect(url_for('index'))

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    Recipe.delete_recipe(id)
    return redirect(url_for('dashboard'))

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    print('/recipes/create  form', request.form)
    
    if not Recipe.validate_recipe(request.form):
        return redirect(url_for('new_recipe'))
  
    # Call the save @classmethod
    recipe_id = Recipe.insert_new_recipe(request.form)
    print('inserted recipe:', recipe_id)
    return redirect(url_for("dashboard"))
 
@app.route('/recipes/update', methods=['POST'])
def update_recipe():
    print('form', request.form)
    
    if not Recipe.validate_recipe(request.form):
        return redirect(url_for('edit_recipe', id=request.form['id']))
  
    # Call the update @classmethod
    Recipe.update_recipe(request.form)
    return redirect(url_for("dashboard"))
