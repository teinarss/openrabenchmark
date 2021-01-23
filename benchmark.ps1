[System.Collections.ArrayList]$params = @(
    'Game.Mod=ra'
    'Engine.EngineDir=..'
     #'Launch.Map=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\maps/ra/{DEV_VERSION}\pathbenchra'
     #'Launch.Map=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\maps/ra/{DEV_VERSION}\treebench'
    'Launch.Replay=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\Replays\ra\{DEV_VERSION}\ra-2021-01-23T151957Z.orarep'
)

$bechparam = "Launch.Benchmark=" 


function runBenchmarks($prefix, [int]$samples) {
    Write-Host $samples
    for($i = 0; $i -lt $samples; $i++)
    {
        $params.Add("$bechparam$prefix$i")
        & "C:\projects\OpenRa\bin\OpenRA.exe" @params
    }
}

Write-Host "euoe"
runBenchmarks  -prefix "pr-" -samples 2
