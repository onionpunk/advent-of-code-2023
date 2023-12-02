# 12 red cubes, 13 green cubes, and 14 blue cubes
$restriction = @{
    "red" = 12;
    "green" = 13;
    "blue" = 14;
}

$sumOfIds = 0

Get-Content .\input.txt | % {
    $validGame = $true
    $line = $_
    $line -match "Game (?<gameNum>.+): (?<gameResults>.+)" | out-null
    $gameNum = [int]$Matches["gameNum"]
    $gameResults =  $Matches["gameResults"] -split ";"
    $gameResults.trim() | % {
        $gameRound = $_ -split ","
        $gameRound | % {
            $colourResult = $_.trim()
            $colourResult -match "(?<quantity>.+) (?<colour>.+)" | out-null
            $quantity = [int]$Matches["quantity"]
            $colour = $Matches["colour"]
            if ($quantity -gt $restriction[$colour]) {
                $validGame = $false
            }
        }
    }

    if ($validGame) {
        $sumOfIds += $gameNum
    }
}

$sumOfIds