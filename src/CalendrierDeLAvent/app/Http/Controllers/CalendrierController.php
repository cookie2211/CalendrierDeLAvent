<?php

namespace App\Http\Controllers;

class CalendrierController extends Controller
{
    public function show(int $jour)
    {
        abort_if($jour < 1 || $jour > 24, 404);

        return view("jour_$jour", [
            'jour' => $jour
        ]);
    }
}
