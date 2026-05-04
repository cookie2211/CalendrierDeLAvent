@extends('layouts.mainLayout')

@section('title', 'Jour 3')

@if($isMobile)
    @section('gameEmplacement', 'demineur_mob/demineur_mob.py')
@else
    @section('gameEmplacement', 'demineur/demineur.py')
@endif

@section('content')
		<p>c'est un démineur, c'est une grille remplie de bombes, 
            l'objectif étant de découvrir toutes les cases sauf celles ou il y a les bombes,
            si on touche une bombe, c'est game over
            le numéro sur une case indique le nombre de bombes sur les cases qui l'entourent
            pour cliquer c'est clic gauche ou double clic (ou clic sur mobile),
            pour poser un drapeau c'est clic droit (ou appui long sur mobile)
        </p>

@endsection