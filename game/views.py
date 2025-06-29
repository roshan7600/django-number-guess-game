from django.shortcuts import render, redirect
import random

# Start or restart the game
def index(request):
    # Only generate a new number if it's not already set (first visit or after restart)
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    return render(request, 'game/index.html')

# Handle guess logic
def guess(request):
    message = ''
    if request.method == 'POST':
        try:
            guess = int(request.POST['guess'])
            number = request.session.get('number')
            request.session['attempts'] += 1

            if guess < number:
                message = 'Too low! Try again.'
            elif guess > number:
                message = 'Too high! Try again.'
            else:
                attempts = request.session["attempts"]
                message = f'🎉 Correct! The number was {number}. You guessed it in {attempts} attempts.'
        except (ValueError, KeyError):
            message = 'Invalid input or session expired. Please restart the game.'

    return render(request, 'game/index.html', {'message': message})

# Restart game view
def restart_game(request):
    request.session.flush()  # Clears the game session
    return redirect('index')
