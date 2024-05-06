from django.shortcuts import render
from .forms import DrillForm
from .utils import generate_arithmetic_drills, validate_answer

def arithmetic_drill(request):
    if request.method == 'POST':
        form = DrillForm(request.POST)
        if form.is_valid():
            num_questions = form.cleaned_data['num_questions']
            min_num = form.cleaned_data['min_num']
            max_num = form.cleaned_data['max_num']
            drills = generate_arithmetic_drills(num_questions, min_num, max_num)
            score = 0
            for i, (question, _) in enumerate(drills, start=1):
                user_answer = request.POST.get(f"answer_{i}")
                if validate_answer(question, user_answer):
                    score += 1
            context = {'drills': drills, 'score': score, 'total_questions': num_questions}
            return render(request, 'arithmetic_drill_app/result.html', context)
    else:
        form = DrillForm()
    return render(request, 'arithmetic_drill_app/arithmetic_drill.html', {'form': form})
