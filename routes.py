from flask import render_template, request, redirect, url_for, flash
from models import db, User

# Placeholder for therapy content - In a real app, this would be from a DB or comprehensive structure
THERAPY_AREAS = {
    'general_neck_relief': {
        'title': 'General Neck Pain Relief',
        'description': 'Gentle exercises to alleviate everyday neck stiffness and discomfort.',
        'exercises': [
            {'id': 'gnr1', 'name': 'Gentle Neck Tilts', 'instructions': 'Slowly tilt your head towards your right shoulder, feeling a gentle stretch on the left side. Hold for 15 seconds. Repeat on the left side. Do 3 repetitions per side. Keep shoulders relaxed.', 'img': 'neck_tilt.jpg'},
            {'id': 'gnr2', 'name': 'Chin Tucks', 'instructions': 'Sit or stand tall. Gently draw your chin back as if making a double chin, keeping your gaze straight. Feel the stretch at the back of your neck. Hold for 5 seconds. Relax. Repeat 10 times.', 'img': 'chin_tuck.jpg'},
            {'id': 'gnr3', 'name': 'Shoulder Rolls', 'instructions': 'Roll your shoulders forward in a circular motion 5 times, then backward 5 times. Keep them relaxed.', 'img': 'shoulder_rolls.jpg'}
        ]
    },
    'posture_improvement': {
        'title': 'Posture Improvement',
        'description': 'Exercises focused on strengthening muscles to improve overall posture.',
        'exercises': [
            {'id': 'pi1', 'name': 'Wall Angels', 'instructions': 'Stand with your back against a wall, feet shoulder-width apart, heels a few inches from the wall. Press your lower back, shoulders, and head against the wall. Raise your arms to shoulder height, elbows bent at 90 degrees, forearms against the wall. Slowly slide your arms up the wall, keeping contact, then back down. Do 10 repetitions.', 'img': 'wall_angels.jpg'},
            {'id': 'pi2', 'name': 'Scapular Squeezes', 'instructions': 'Sit or stand tall. Gently squeeze your shoulder blades together as if holding a pencil between them. Keep your shoulders down, not shrugging. Hold for 5 seconds. Relax. Repeat 10-15 times.', 'img': 'scapular_squeezes.jpg'}
        ]
    },
    # Add more therapy areas here (e.g., 'upper_back_tension', 'stretches_for_stiffness')
}

def init_app_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/disclaimer')
    def disclaimer():
        return render_template('disclaimer.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            # Basic validation
            if not username or not email or not password:
                flash('All fields are required!', 'error')
                return render_template('signup.html')

            if User.query.filter_by(username=username).first():
                flash('Username already exists!', 'error')
                return render_template('signup.html')

            if User.query.filter_by(email=email).first():
                flash('Email already exists!', 'error')
                return render_template('signup.html')

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! You can now start your therapy.', 'success')
            return redirect(url_for('therapy_selection'))
        return render_template('signup.html')

    @app.route('/therapy')
    def therapy_selection():
        return render_template('therapy_selection.html', areas=THERAPY_AREAS)

    @app.route('/therapy/<area_id>')
    def therapy_intro(area_id):
        area = THERAPY_AREAS.get(area_id)
        if not area:
            flash('Therapy area not found!', 'error')
            return redirect(url_for('therapy_selection'))
        return render_template('therapy_intro.html', area=area, area_id=area_id)

    @app.route('/therapy/<area_id>/exercise/<exercise_index>')
    def exercise_detail(area_id, exercise_index):
        area = THERAPY_AREAS.get(area_id)
        if not area:
            flash('Therapy area not found!', 'error')
            return redirect(url_for('therapy_selection'))

        try:
            current_exercise_index = int(exercise_index)
            exercise = area['exercises'][current_exercise_index]
        except (ValueError, IndexError):
            flash('Exercise not found!', 'error')
            return redirect(url_for('therapy_intro', area_id=area_id))

        next_exercise_index = current_exercise_index + 1
        has_next = next_exercise_index < len(area['exercises'])

        return render_template(
            'exercise_detail.html',
            area=area,
            area_id=area_id,
            exercise=exercise,
            current_index=current_exercise_index,
            next_index=next_exercise_index,
            has_next=has_next
        )

    @app.route('/therapy/<area_id>/complete')
    def therapy_complete(area_id):
        area = THERAPY_AREAS.get(area_id)
        if not area:
            flash('Therapy area not found!', 'error')
            return redirect(url_for('therapy_selection'))
        return render_template('therapy_complete.html', area=area)
