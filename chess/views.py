from django.shortcuts import render

def chess_dashboard(request):
    return render(request, 'chess/chess_dashboard.html')

def play_chess(request):
    # Logic to render chess game
    return render(request, 'chess/play_chess.html')
