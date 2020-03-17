[System.Collections.ArrayList]$params = @(
    'Game.Mod=ra'
     'Launch.Map=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\maps/ra/{DEV_VERSION}\pathbenchra'
     #'Launch.Map=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\maps/ra/{DEV_VERSION}\treebench'
    #'Launch.Replay=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\Replays\ra\{DEV_VERSION}\OpenRA-2019-06-06T141718Z.orarep'
)

$bechparam = "Launch.Benchmark=" 


function runBenchmarks($prefix, [int]$samples) {
    Write-Host $samples
    for($i = 0; $i -lt $samples; $i++)
    {
        $params.Add("$bechparam$prefix$i")
        & "C:\projects\OpenRa1\OpenRa.Game.exe" @params
    }
}

Write-Host "euoe"
runBenchmarks  -prefix "bleed-renderble-" -samples 5
