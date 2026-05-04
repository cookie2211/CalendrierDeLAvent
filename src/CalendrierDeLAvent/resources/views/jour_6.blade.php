@extends('layouts.mainLayout')

@section('title', 'Jour 6')

@section('gameEmplacement', 'Pac_man/Pac_Man.py')

@section('content')
		<p>il s'agit du célèbre jeu Pac Man, 
            pour gagner il faut ramasser toutes les pieces du labyrinthe, 
            si on touche un fantôme c'est game over.
            les cerises rapportent des points supplémentaires.
            pour bouger il faut rester appuyé sur les touches directionnelles ou les flèches du gamepad.
            il y a un passage de téléportation au bord milieu droit qui va vers le bord milieu gauche, et inversement
        </p>

@endsection