from django.shortcuts import render

def start_test(request):
    return render(request, 'test/start_test.html')

def test_questions(request):
    # Logic to render questions
    return render(request, 'test/test_questions.html')

def test_results(request):
    # Logic to calculate and render results
    return render(request, 'test/test_results.html')
