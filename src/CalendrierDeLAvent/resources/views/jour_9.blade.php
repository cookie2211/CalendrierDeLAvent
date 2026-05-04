@extends('layouts.mainLayout')

@section('title', 'Jour 9')

@section('gameEmplacement', 'snake/snake.py')

@section('content')
		<p>c'est un snake, le but est d'avaler le plus de pommes possibles
            pour les manger il faut faire aller le serpent sur la case de la pomme,
            il grandit a chaque fois qu'il en avale une.
            pour faire bouger le serpend on utilise les flèches directionnelles ou les flèches du gamepad
            si on heurte le bord de la fenêtre ou qu'on heurte le corps du serpent, c'est game over.
            vôtre score s'affiche a la fin
        </p>

@endsection