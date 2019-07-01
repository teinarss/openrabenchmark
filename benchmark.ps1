[System.Collections.ArrayList]$params = @(
    'Game.Mod=ra'
     'Launch.Map=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\maps/ra/{DEV_VERSION}\pathbenchra'
    #'Launch.Replay=C:\Users\Tomas.PYTTEMJUK\Documents\OpenRA\Replays\ra\{DEV_VERSION}\OpenRA-2019-06-06T141718Z.orarep'
)

$bechparam = "Launch.Benchmark=" 


function runBenchmarks($prefix, [int]$samples) {
    Write-Host "uiuiui"
    Write-Host $samples
    for($i = 0; $i -lt $samples; $i++)
    {
        Write-Host "llll"
        $params.Add("$bechparam$prefix$i")
        & "C:\projects\OpenRa1\OpenRA.Game.exe" @params
    }
}

Write-Host "euoe"
runBenchmarks  -prefix "no-flags-class-" -samples 5
