<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CalendrierController extends Controller
{
    public function show(Request $request, int $jour)
    {
        abort_if($jour < 1 || $jour > 24, 404);

        $isMobile = preg_match(
            '/Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/i',
            $request->userAgent()
        );

        return view("jour_$jour", [
            'jour' => $jour,
            'isMobile' => $isMobile
        ]);
    }
}
