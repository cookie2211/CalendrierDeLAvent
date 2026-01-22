<?php

namespace App\Http\Controllers;

class CalendrierController extends Controller
{
    public function show(int $jour)
    {
        // Sécurité : empêcher jour < 1 ou > 24
        abort_if($jour < 1 || $jour > 24, 404);

        return view('jour', [
            'jour' => $jour
        ]);
    }
}
